from SimpleCV import *

img = Image("./parking_full.png")

img = img / 2
img = img.edges(25, 400)

img.save("parking_edge.png")

num_spots = 0


spots = [
    [(0, 420), (130, 461), (235, 419), (73, 374)],
    [(68, 374), (247, 422), (326, 378), (170, 338)],
    [(170, 338), (322, 380), (398, 350), (242, 320)],
    [(230, 300), (403, 352), (456, 313), (328, 248)]
]

full_mask = Image(img.size())
draw_full = DrawingLayer(img.size())
draw_full.polygon([(0,0), (0, 960), (1280, 960), (1280, 0)], filled=True, color=Color.WHITE)
full_mask.addDrawingLayer(draw_full)
full_mask = full_mask.applyLayers()
i = 0
for s in spots:

    mask_spot = Image(img.size())
    draw_spot = DrawingLayer(img.size())

    draw_spot.polygon(s, filled=True, color=Color.WHITE)

    mask_spot.addDrawingLayer(draw_spot)
    mask_spot = mask_spot.applyLayers()

    masked_img = (img - (full_mask - mask_spot))

    img_matrix = masked_img.getNumpy().flatten()
    img_pixel_count = cv2.countNonZero(img_matrix)

    print "Pixel count %d" % img_pixel_count
    if img_pixel_count < 1500:
        print "Spot found"
        num_spots = num_spots + 1
    masked_img.save("./parking_%d.png" % i)
    i = i + 1

print "Found %d spots" % num_spots