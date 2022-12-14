# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401
from libqtile import layout, bar, widget, hook

from bar import screens, widget_defaults
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from colors import nord_fox
from unicodes import lower_left_triangle

mod = "mod4"
terminal = "kitty"
myBrowser = "librewolf"
myGames = "lutris"
myGames2 = "steam"
Teams = "teams"
Messenger1 = "element-desktop"
Messenger2 = "discord"
Screenshot = "scrot"
PlayOsuGame = "osu-wine"
Music = "spotify"

#GameMode = "pkill picom"
#DisableGameMode "picom --experimental-backends"

keys = [
     Key([mod], "p",
             lazy.spawn("rofi -modi drun,run -show drun 'Run: '"),
             desc='Run Launcher'
 ),

 Key([mod], "b",
             lazy.spawn(myBrowser),
             desc='librewolf'
             ),

               Key([mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),

  Key([mod, "shift"], "F5",
  lazy.spawn(myGames)

  ),

  Key([mod, "shift"], "c",
             lazy.window.kill(),
             desc='Kill active window'
             ),


  Key([mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),

  Key([mod, "shift"], "F6",
  lazy.spawn(Teams)

  ),


  Key([mod], "F5",
  lazy.spawn(Messenger1)

  ),


  Key([mod], "d",
  lazy.spawn(Messenger2)

  ),

  Key([mod], "s",
             lazy.spawn(Screenshot)
             ),

Key([mod, "shift"], "s",
        lazy.spawn(myGames2)

        ),


Key([mod, "shift"], "o",
        lazy.spawn(PlayOsuGame)

        ),

  Key([mod, "control"], "s",
        lazy.spawn(Music)

        ),

# Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]



groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
      
        ])
layouts = [
    layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=0,
        margin = 8),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(), 
    layout.Max(margin = 8), 
    layout.MonadTall(
        margin=13, border_width=1 ),
     layout.MonadWide(margin = 8, border_width=0),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # Layout.Zoomy(),
    # layout.Columns(margin = 8),

    ]

widget_defaults = dict(
        font='JetBrainsMono',
    fontsize=12,
    padding=3,
   background=nord_fox["bg"],
    foreground=nord_fox["fg"],

)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [                
                         
             
          

                   widget.Image(
                       filename = "~/.config/qtile/python-white.png",
                       scale = "False",
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal)},
                       background = nord_fox["black"],



                       ),



                widget.GroupBox( active=nord_fox["fg"],
                    inactive=nord_fox["fg_gutter"],
                    disable_drag=True,
                    borderwidth=0,
                    margin_x=0,
                    padding_x=10,
                    highlight_method="line",
                    block_highlight_text_color=nord_fox["red"],
                    highlight_color=nord_fox["bg"],
                    ),


               
                 
                widget.Prompt(),
                

                widget.WindowName(),
                

                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    
           

                        },
                    name_transform=lambda name: name.upper(),
                

                    ),
               

widget.Systray (

    background = nord_fox["black"],  
    padding = 5

    ), 
                

                
            widget.Volume(
                       foreground = nord_fox["magenta"],
                       background = nord_fox["black"],
                       padding = 5
                       ),

                widget.Memory(
                    foreground=nord_fox["pink"],
                    padding=10,
                    measure_mem="G",
                    format=" {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}",
                    background=nord_fox['black']
                ),



                widget.CPU(

                    foreground=nord_fox["yellow"],
                    padding=10,
                    format=" {freq_current}GHz {load_percent}%",
                    background=nord_fox['black']
                ),
           

             widget.Clock(
foreground=nord_fox["red"],
format="??? %Y-%m-%d %a %I:%M %p",
padding=10,
background=nord_fox['black']
),

 widget.Net(
                    foreground=nord_fox["green"],
                    interface="wlp61s0",
                    format="{down} ?????? {up}",
                    background=nord_fox['black']
                ),





widget.DF(
                    format="??? {p} {uf}",
                    visible_on_warn=False,
                    foreground=nord_fox["blue"],
                    background=nord_fox['black']
                ),


                
 widget.CurrentLayout(
                    foreground=nord_fox["magenta"],
                    background=nord_fox["black"],
                    fmt="[{}]",
                    padding=10,
                ),


                                              
                                           
              ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        
                     ),

       ),

   ]


        # Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + 'autostart.sh'])


# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "qtile"



