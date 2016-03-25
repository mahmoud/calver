# user customization
# TODO: document other hooks

import os

print ' - custom module loaded.'


def chert_post_load(chert_obj):
    print ' - post_load hook: %s entries loaded' % len(chert_obj.entries)
    _autotag_entries(chert_obj)


def chert_pre_audit(chert_obj):
    # exceptions are automatically caught and logged
    # just enable debug mode to see issues
    raise ValueError('something went awry')


def _autotag_entries(chert_obj):
    # called by post_load
    for entry in chert_obj.entries:
        rel_path = os.path.relpath(entry.input_path, chert_obj.entries_path)
        rel_path, entry_filename = os.path.split(rel_path)
        new_tags = [p.strip() for p in rel_path.split('/') if p.split()]
        for tag in new_tags:
            if tag not in entry.tags:
                entry.tags.append(tag)

    chert_obj._rebuild_tag_map()

    return
