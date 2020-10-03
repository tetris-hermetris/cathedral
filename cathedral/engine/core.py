## PSEUDOCODE

# scenario = [
#     {start: 0, end: 120, scenes: [dancing_lizard, singing_star]},
#     {start: 120, end: 140, ctime: 120, scenes: [dancing_lizard, singing_star]},
#     {start: 10, end: 50, scenes: [broken_window, drunk_panda]}
# ]

# def dancing_lizard(time, context, ...):
#     pass

# def engine():
#     context = {}
#     frame = 0
#     while frame < duration*fps:
#         time = frame/fps
#         for {start, end, scenes, ctime} in scenario:
#             if start <= time <= end:
#                 for scene in scenes:
#                     figure = scene(ctime or time, context, ...)
#                     add_figure_to_frame(content, figure)
#         post_processing(time, content)
#         render_frame(content)
#         frame += 1
