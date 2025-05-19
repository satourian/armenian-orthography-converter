import json
import re
import importlib.resources as resources

with resources.open_text('armenian_orthography_converter.data', 'export.json', encoding='utf-8') as f:
    _RAW = json.load(f)

def _fix_repl(s):
    return re.sub(r'\$(\d)', r'\\\1', s)

_DATA = [(
    re.compile(src), _fix_repl(repl),
    re.compile(rsrc), _fix_repl(rrepl)
) for src, repl, rsrc, rrepl in _RAW['data']]

_WORDS_PARTS = [(re.compile(src), _fix_repl(repl)) for src, repl in _RAW['wordsParts']]
_WORDS_PARTS_REV = [(re.compile(repl), _fix_repl(src)) for src, repl in _RAW['wordsParts']]

_ERR_SOV_MASH = [(re.compile(src), _fix_repl(repl)) for src, repl in _RAW['errorCorrectionSovietToMashtots']]
_ERR_SOV_MASH_WORD = [(re.compile(src), _fix_repl(repl)) for src, repl in _RAW['errorCorrectionSovietToMashtotsInTheWord']]

_ERR_MASH_SOV = [(re.compile(src), _fix_repl(repl)) for src, repl in _RAW['errorCorrectionMashtotsToSoviet']]
_ERR_MASH_SOV_WORD = [(re.compile(src), _fix_repl(repl)) for src, repl in _RAW['errorCorrectionMashtotsToSovietInTheWord']]

def _apply_rules(text, rules, show):
    for expr, repl in rules:
        new_text = expr.sub(repl, text)
        if show and new_text != text:
            print(f"{text}->{new_text} ({expr.pattern})")
        text = new_text
    return text

def soviet_to_mashtots(text, show_path=False):
    text = _apply_rules(text, _WORDS_PARTS, show_path)
    for fwd, repl, _, _ in _DATA:
        text = _apply_rules(text, [(fwd, repl)], show_path)
    text = _apply_rules(text, _ERR_SOV_MASH_WORD, show_path)
    for expr, repl in _ERR_SOV_MASH:
        pattern = re.compile(f"(^|{_RAW['start']})" + expr.pattern + f"({_RAW['end']})")
        new_text = pattern.sub(lambda m: m.group(1) + repl + m.group(2), text)
        if show_path and new_text != text:
            print(f"{text}->{new_text} ({pattern.pattern})")
        text = new_text
    return text

def mashtots_to_soviet(text, show_path=False):
    # reverse rules from wordsParts
    text = _apply_rules(text, _WORDS_PARTS_REV, show_path)
    for fwd, repl, rsrc, rrepl in reversed(_DATA):
        text = _apply_rules(text, [(rsrc, rrepl)], show_path)
    text = _apply_rules(text, _ERR_MASH_SOV_WORD, show_path)
    for expr, repl in _ERR_MASH_SOV:
        pattern = re.compile(f"(^|{_RAW['start']})" + expr.pattern + f"({_RAW['end']})")
        new_text = pattern.sub(lambda m: m.group(1) + repl + m.group(2), text)
        if show_path and new_text != text:
            print(f"{text}->{new_text} ({pattern.pattern})")
        text = new_text
    return text
