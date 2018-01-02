# -*- coding: utf8 -*-

from xlwt import *


class _Excel(object):
    @staticmethod
    def get_header_2_style():
        header_2_fnt = Font()
        header_2_fnt.bold = True
        header_2_fnt.height = 14 * 14
        header_2_style = XFStyle()
        header_2_style.font = header_2_fnt
        header_2_alignment = Alignment()
        header_2_alignment.horz = Alignment.HORZ_CENTER
        header_2_style.alignment = header_2_alignment
        return header_2_style

    @staticmethod
    def append_row(sheet, row_index=None, style=None, cell_width=None, *cells):
        if row_index is None:
            row_index = len(sheet.rows)
        row = sheet.row(row_index)
        for c, cell in enumerate(cells):
            if cell is not None and cell != '':
                if style is not None:
                    row.write(c, cell, style)
                    if cell_width is not None:
                        sheet.col(c).width = cell_width
                else:
                    row.write(c, cell)
