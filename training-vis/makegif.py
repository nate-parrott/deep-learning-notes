# import moviepy.editor as mpy
import json

txt = open('training.txt').read()
parts = [p.split(' example encoding')[0] for p in txt.split('Step: ') if len(p.strip()) > 0]

def pad_str(s, size=14):
    if len(s) > size:
        return s[:size]
    else:
        return s + ' ' * (size - len(s))

def process_part(part):
    step = part.split(';')[0]
    content = part.split('\n', 1)[1].strip()
    pairs = [('NAME', 'RECONSTRUCTION')] + [line.split(' -> ') for line in content.split('\n')]
    lines = "\n".join([pad_str(a) + pad_str(b) for a, b in pairs])
    return "Step {0}\n{1}".format(step, lines)

parts = map(process_part, parts)
open('parts.js', 'w').write("parts = " + json.dumps(parts))
quit()

screensize = (720,460)
color = mpy.ColorClip(screensize, (255,255,255), duration=2)
txt_clip = mpy.TextClip(parts[0], size=screensize, color='#FF0096', font="../GT-Pressura-Mono-Regular.ttf", fontsize=50, align='West')
txt_clip = txt_clip.set_position((20, 50)).set_duration(2)

comp = mpy.CompositeVideoClip([color, txt_clip])

comp.write_gif("test.gif", fps=10)
