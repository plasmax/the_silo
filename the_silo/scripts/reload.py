import nuke

def all_reads():
    """Reload all read nodes in the compositing script"""
    for node in nuke.allNodes():
        if node.Class() == 'Read':
            node.knob('reload').execute()
