import math
def generate_anchors(feature_size: int, image_size: float, scales: list[float], aspect_ratios: list[float]) -> list[list[float]]:
    """
    Returns a list of [x1, y1, x2, y2] anchor boxes.
    """
    #Cell (0,0):\[c_x=(0+0.5)\times4=2\]
#               \[c_y=(0+0.5)\times4=2\] = (2,2)
# for cell (0,1),(1,0)and(1,1) = (6,2),(2,6)and(6,6)
# given aspect ratio :- 0.5,1,2 ==> \[w=s\sqrt{r}\] and \[h=\frac{s}{\sqrt{r}}\]

    stride = image_size / feature_size
    anchors = []
    for i in range(feature_size):
        for j in range(feature_size):
            cx = (j+0.5)*stride
            cy = (i+0.5)*stride
            for s in scales:
                for r in aspect_ratios:
                    w = s*math.sqrt(r)
                    h = s/math.sqrt(r)
                    anchors.append([cx-w/2,cy-h/2,cx+w/2,cy+h/2])
    return anchors