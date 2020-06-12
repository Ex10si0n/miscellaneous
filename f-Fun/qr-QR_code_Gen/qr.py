#!/usr/bin/env python
# -*- coding: utf-8 -*-

from MyQR import myqr
myqr.run(
    words=input('Target: '),
    colorized=True,
    save_name=input('Save Name: ')+'.png'
)
