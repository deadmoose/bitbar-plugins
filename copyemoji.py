#!/usr/bin/env python
# -*- coding: utf-8 -*-
# <bitbar.title>EMOJI!</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>David Hoover</bitbar.author>
# <bitbar.author.github>deadmoose</bitbar.author.github>
# <bitbar.desc>Handy copy & paste of emoji</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>

import subprocess
import sys

EMOJI = (
    u'¯\_(ツ)_/¯',
    u'💩',
    u'☃',
)

if len(sys.argv) < 2:
    # No args = dump a bitbar-friendly index of these
    print EMOJI[0].encode('utf-8')
    print "---"
    for i, emoji in enumerate(EMOJI):
        print '%s | terminal=false bash=%s param1=%s' % (emoji.encode('utf-8'),
                                                         sys.argv[0], i)
else:
    # Dump the Nth emoji into the clipboard
    emoji = EMOJI[int(sys.argv[1])]
    p = subprocess.Popen(
        ['/usr/bin/pbcopy'],
        stdin=subprocess.PIPE,
        env={
            'LANG': 'en_US.UTF-8'
        })
    p.communicate(emoji.encode('utf-8'))
