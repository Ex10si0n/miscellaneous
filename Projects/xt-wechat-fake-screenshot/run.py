#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
for iden in range(1, 52):
    bgsrc = "src/p"+str(iden)+".PNG"
    bg = Image.open(bgsrc)
    xt = Image.open("sbxt.PNG")
    sbxt = xt.load()
    xt_x, xt_y = xt.size[0], xt.size[1]
    bg_px = bg.load()
    bg_x, bg_y = bg.size[0], bg.size[1]
    corner_x, corner_y = 0, 0
    print("Read Info: x, y is ", bg_x, bg_y)

    # Find Link Top-Left Corner
    link_corner_found = False
    for i in range(0, bg_x):
        for j in range(0, bg_y):
            r, g, b, a = bg_px[i, j][0], bg_px[i, j][1], bg_px[i, j][2], bg_px[i,j][3]
            r1, g1, b1, a1 = 0, 0, 0, 0
            if i+10 < bg_x:
                r1, g1, b1, a1 = bg_px[i+10, j][0], bg_px[i+10, j][1], bg_px[i+10,j][2],bg_px[i+10, j][3]
            if (r, g, b, a) == (243, 243, 245, 255) and (r1, g1, b1, a1) == (243, 243, 245, 255):
                corner_x, corner_y = i, j
                link_corner_found = True
                break
        if link_corner_found:
            break

    # Delete Origin User Info

    for i in range(0, bg_x):
        for j in range(0, corner_y):
            bg_px[i, j] = (255, 255, 255, 255)
    for i in range(0, corner_x):
        for j in range(0, bg_y):
            bg_px[i, j] = (255, 255, 255, 255)

    # Find XT's Corner
    xt_corner_found = False
    xt_corner_x, xt_corner_y = 0, 0;
    for i in range(0, xt_x):
        for j in range(0, xt_y):
            r, g, b, a = sbxt[i, j][0], sbxt[i, j][1], sbxt[i, j][2], sbxt[i,j][3]
            if (r, g, b, a) == (0, 0, 0, 0):
                xt_corner_x, xt_corner_y = i, j;
                xt_corner_found = True
                break
        if xt_corner_found:
            break

    # Merge with underground as bg
    offset_x = corner_x-xt_corner_x
    offset_y = corner_y-xt_corner_y
    if offset_x < 0:
        offset_x = 0
    if offset_y < 0:
        offset_y = 0
    print(offset_x, offset_y)
    for i in range(offset_x+1, bg_x):
        for j in range(offset_y+1, bg_y):
            sbxt_x = i-offset_x
            sbxt_y = j-offset_y
            if i >= corner_x and j >= corner_y:
                break
            if sbxt_x > xt_x or sbxt_y > xt_y:
                break
            if i > bg_y or j > bg_y:
                break
            bg_px[i, j] = sbxt[sbxt_x-1, sbxt_y-1]
    savesrc = "out/IMG_13"+str(iden)+".PNG"
    bg_save = bg.save(savesrc, "PNG")
    print("Done")
