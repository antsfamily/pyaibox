def plot_bbox(bboxes, labels=None, scores=None, edgecolors=None, linewidths=1, fontdict=None, textpos='TopCenter', offset=None, ax=None):
    r"""Plots bounding boxes with scores and labels


    Parameters
    ----------
    bboxes : list or numpy array
        The bounding boxes, in ``LeftTopRightBottom`` mode, which means (xmin, ymin, xmax, ymax)
    labels : list or None, optional
        The labels, can be a list of class id or class name. If None, won't show labels. scores : list or None, optional
    """
    nbox = len(bboxes)
    labels = [labels] * nbox if labels is None or type(labels) is str else labels
    labels = labels * nbox if len(labels) == 1 else labels
    scores = [scores] * nbox if scores is None or type(scores) is float else scores
    scores = scores * nbox if len(scores) == 1 else scores
    # edgecolors = pb.DISTINCT_COLORS['DistinctNormRGB20'][slice(0, nbox)] if edgecolors is None else edgecolors
    edgecolors = [edgecolors] * nbox if edgecolors is None else edgecolors
    edgecolors = edgecolors * nbox if len(edgecolors) == 1 else edgecolors
    edgecolors = [edgecolors] * nbox if type(edgecolors) is str or len(edgecolors) != nbox else edgecolors

    linewidths = [linewidths] * nbox if type(linewidths) is float or type(linewidths) is int or linewidths is None else linewidths
    linewidths = linewidths * nbox if len(linewidths) == 1 else linewidths
    offset = [6, 0] if offset is None else offset
    offset = [offset] * 2 if type(offset) is int or type(offset) is float else offset

    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

    for bbox, label, score, edgecolor, linewidth in zip(bboxes, labels, scores, edgecolors, linewidths):
        xy = (bbox[1], bbox[0])
        height = bbox[2] - bbox[0]
        width = bbox[3] - bbox[1]
        ax.add_patch(plt.Rectangle(xy, width, height, fill=False, edgecolor=edgecolor, linewidth=linewidth))
        caption = ''
        if label is not None:
            caption += str(label)
        if score is not None:
            caption += ': {:.2f}'.format(score)

        if textpos in ['TopCenter', 'topcenter']:
            ax.text(bbox[1] + width / 2 - offset[1], bbox[0] - offset[0], caption, fontdict=fontdict)
        if textpos in ['BottomCenter', 'bottomcenter']:
            ax.text(bbox[1] + width / 2 - offset[1], bbox[2] + offset[0], caption, fontdict=fontdict)
        if textpos in ['TopLeft', 'topleft']:
            ax.text(bbox[1] - offset[1], bbox[0] - offset[0], caption, fontdict=fontdict)
        if textpos in ['BottomLeft', 'bottomleft']:
            ax.text(bbox[1] - offset[1], bbox[2] + offset[0], caption, fontdict=fontdict)
    return ax


# def fmt_bbox(bboxes, fmtstr='LTRB2CHW'):
#     r"""Formats bounding boxes

#     .. warning:: The height and width are computed by :math:`y_{\rm max} - y_{\rm min}` and :math:`x_{\rm max} - x_{\rm min}`.


#     Parameters
#     ----------
#     bboxes : list or numpy array
#         The bounding boxes to be converted, all bboxes have the same mode.
#     fmtstr : str, optional
#         - ``'LTRB2TLBR'``: LeftTopRightBottom (xmin, ymin, xmax, ymax) --> TopLeftBottomRight (ymin, xmin, ymax, xmax)
#         - ``'TLBR2LTRB'``: TopLeftBottomRight (ymin, xmin, ymax, xmax) --> LeftTopRightBottom (xmin, ymin, xmax, ymax)
#         - ``'CWH2CHW'``: CenterWidthHeight (x, y, w, h) --> CenterHeightWidth (y, x, h, w)
#         - ``'CHW2CWH'``: CenterHeightWidth (y, x, h, w) --> CenterWidthHeight (x, y, w, h)
#         - ``'LTRB2CWH'``: LeftTopRightBottom (xmin, ymin, xmax, ymax) --> CenterWidthHeight (x, y, w, h)
#         - ``'LTRB2CHW'``: LeftTopRightBottom (xmin, ymin, xmax, ymax) --> CenterHeightWidth (y, x, h, w)
#         - ``'TLBR2CWH'``: TopLeftBottomRight (ymin, xmin, ymax, xmax) --> CenterWidthHeight (x, y, w, h)
#         - ``'TLBR2CHW'``: TopLeftBottomRight (ymin, xmin, ymax, xmax) --> CenterHeightWidth (y, x, h, w)
#         - ``'CWH2LTRB'``: CenterWidthHeight (x, y, w, h) --> LeftTopRightBottom (xmin, ymin, xmax, ymax)
#         - ``'CWH2TLBR'``: CenterWidthHeight (x, y, w, h) --> TopLeftBottomRight (ymin, xmin, ymax, xmax)
#         - ``'CHW2LTRB'``: CenterHeightWidth (y, x, h, w) --> LeftTopRightBottom (xmin, ymin, xmax, ymax)
#         - ``'CHW2TLBR'``: CenterHeightWidth (y, x, h, w) --> TopLeftBottomRight (ymin, xmin, ymax, xmax)
#         - ``'LRTB2LTRB'``: LeftRightTopBottom (xmin, xmax, ymin, ymax) --> LeftTopRightBottom (xmin, ymin, xmax, ymax)
#         - ``'LRTB2TLBR'``: LeftRightTopBottom (xmin, xmax, ymin, ymax) --> TopLeftBottomRight (ymin, xmin, ymax, xmax)
#         - ``'LTRB2LRTB'``: LeftTopRightBottom (xmin, ymin, xmax, ymax) --> LeftRightTopBottom (xmin, xmax, ymin, ymax)
#         - ``'LRTB2CWH'``: LeftRightTopBottom (xmin, xmax, ymin, ymax) --> CenterWidthHeight (x, y, w, h)
#         - ``'LRTB2CHW'``: LeftRightTopBottom (xmin, xmax, ymin, ymax) --> CenterHeightWidth (y, x, h, w)
#         - ``'CWH2LRTB'``: CenterWidthHeight (x, y, w, h) --> LeftRightTopBottom (xmin, xmax, ymin, ymax)
#         - ``'CHW2LRTB'``: CenterHeightWidth (y, x, h, w) --> LeftRightTopBottom (xmin, xmax, ymin, ymax)

#     Returns
#     -------
#     list or numpy array
#         The formated bounding boxes.

#     see :func:`plot_bbox`

#     """

def fmt_bbox(bboxes, fmtstr='LTRB2CHW'):
    r"""Formats bounding boxes

    .. warning:: The height and width are computed by :math:`y_{\rm max} - y_{\rm min}` and :math:`x_{\rm max} - x_{\rm min}`.


    Parameters
    ----------
    bboxes : list or numpy array
        The bounding boxes to be converted, all bboxes have the same mode.
    fmtstr : str, optional
        - ``'LTRB2TLBR'``: LeftTopRightBottom (xmin, ymin, xmax, ymax) --> TopLeftBottomRight (ymin, xmin, ymax, xmax)
        - ``'TLBR2LTRB'``: TopLeftBottomRight (ymin, xmin, ymax, xmax) --> LeftTopRightBottom (xmin, ymin, xmax, ymax)
        - ``'CWH2CHW'``: CenterWidthHeight (x, y, w, h) --> CenterHeightWidth (y, x, h, w)
        - ``'CHW2CWH'``: CenterHeightWidth (y, x, h, w) --> CenterWidthHeight (x, y, w, h)
        - ``'LTRB2CWH'``: LeftTopRightBottom (xmin, ymin, xmax, ymax) --> CenterWidthHeight (x, y, w, h)
        - ``'LTRB2CHW'``: LeftTopRightBottom (xmin, ymin, xmax, ymax) --> CenterHeightWidth (y, x, h, w)
        - ``'TLBR2CWH'``: TopLeftBottomRight (ymin, xmin, ymax, xmax) --> CenterWidthHeight (x, y, w, h)
        - ``'TLBR2CHW'``: TopLeftBottomRight (ymin, xmin, ymax, xmax) --> CenterHeightWidth (y, x, h, w)
        - ``'CWH2LTRB'``: CenterWidthHeight (x, y, w, h) --> LeftTopRightBottom (xmin, ymin, xmax, ymax)
        - ``'CWH2TLBR'``: CenterWidthHeight (x, y, w, h) --> TopLeftBottomRight (ymin, xmin, ymax, xmax)
        - ``'CHW2LTRB'``: CenterHeightWidth (y, x, h, w) --> LeftTopRightBottom (xmin, ymin, xmax, ymax)
        - ``'CHW2TLBR'``: CenterHeightWidth (y, x, h, w) --> TopLeftBottomRight (ymin, xmin, ymax, xmax)
        - ``'LRTB2LTRB'``: LeftRightTopBottom (xmin, xmax, ymin, ymax) --> LeftTopRightBottom (xmin, ymin, xmax, ymax)
        - ``'LRTB2TLBR'``: LeftRightTopBottom (xmin, xmax, ymin, ymax) --> TopLeftBottomRight (ymin, xmin, ymax, xmax)
        - ``'LTRB2LRTB'``: LeftTopRightBottom (xmin, ymin, xmax, ymax) --> LeftRightTopBottom (xmin, xmax, ymin, ymax)
        - ``'LRTB2CWH'``: LeftRightTopBottom (xmin, xmax, ymin, ymax) --> CenterWidthHeight (x, y, w, h)
        - ``'LRTB2CHW'``: LeftRightTopBottom (xmin, xmax, ymin, ymax) --> CenterHeightWidth (y, x, h, w)
        - ``'CWH2LRTB'``: CenterWidthHeight (x, y, w, h) --> LeftRightTopBottom (xmin, xmax, ymin, ymax)
        - ``'CHW2LRTB'``: CenterHeightWidth (y, x, h, w) --> LeftRightTopBottom (xmin, xmax, ymin, ymax)

    Returns
    -------
    list or numpy array
        The formated bounding boxes.

    see :func:`plot_bbox`

    """


