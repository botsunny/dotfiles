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

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from pipe_volume import Volume

mod = "mod4"
terminal = "alacritty"

nord = [
        # Polar Night
        "#2e3440", # 0
        "#3b4252", # 1
        "#434c5e", # 2
        "#4c566a", # 3

        # Snow Storm
        "#d8dee9", # 4
        "#e5e9f0", # 5
        "#eceff4", # 6

        # Frost
        "#8fbcbb", # 7
        "#88c0d0", # 8
        "#81a1c1", # 9
        "#5e81ac", # 10

        # Aurora
        "#bf616a", # 11
        "#d08770", # 12
        "#ebcb8b", # 13
        "#a3be8c", # 14
        "#b48ead", # 15
       ]

@lazy.function
def grow_monad(qtile, direction):
    layout = qtile.current_layout
    
    if layout.name == "monadtall":
        tall = True
    elif layout.name == "monadwide":
        tall = False
    else:
        return
        
    if direction == "left":
        return layout.cmd_shrink_main() if tall else layout.cmd_shrink()
    elif direction == "right":
        return layout.cmd_grow_main() if tall else layout.cmd_grow()
    elif direction == "down":
        return layout.cmd_shrink() if tall else layout.cmd_grow_main()
    elif direction == "up":
        return layout.cmd_grow() if tall else layout.cmd_shrink_main()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    # Switch between windows
    Key([mod], "Left",
        lazy.layout.left(),
        desc="Move focus to left"),
    Key([mod], "Right",
        lazy.layout.right(),
        desc="Move focus to right"),
    Key([mod], "Down",
        lazy.layout.down(),
        desc="Move focus down"),
    Key([mod], "Up",
        lazy.layout.up(),
        desc="Move focus up"),
    Key([mod], "h",
        lazy.layout.left(),
        desc="Move focus to left"),
    Key([mod], "l",
        lazy.layout.right(),
        desc="Move focus to right"),
    Key([mod], "j",
        lazy.layout.down(),
        desc="Move focus down"),
    Key([mod], "k",
        lazy.layout.up(),
        desc="Move focus up"),
    Key([mod], "space",
        lazy.layout.next(),
        desc="Move window focus to other window"),
    Key([mod, "shift"], "space",
        lazy.layout.previous(),
        desc="Move window focus to previous window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left",
        lazy.layout.shuffle_left(), lazy.layout.decrease_ratio(),
        desc="Move window to the left, decrease ratio (ratiotile)"),
    Key([mod, "shift"], "Right",
        lazy.layout.shuffle_right(), lazy.layout.increase_ratio(),
        desc="Move window to the right, increase ratio (ratiotile)"),
    Key([mod, "shift"], "Down",
        lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up",
        lazy.layout.shuffle_up(),
        desc="Move window up"),
    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left(), lazy.layout.decrease_ratio(),
        desc="Move window to the left, decrease ratio (ratiotile)"),
    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(), lazy.layout.increase_ratio(),
        desc="Move window to the right, increase ratio (ratiotile)"),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc="Move window up"),
    Key([mod, "control"], "space",
        lazy.layout.swap_main(),
        desc=""),
    Key([mod, "shift", "control"], "space",
        lazy.layout.flip(),
        desc="Switch main pane alignment"),
    
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(), grow_monad(direction="left"),
        desc="Grow window to the left, shrink main pane (monadtall), shrink window (monadwide)"),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(), grow_monad(direction="right"),
        desc="Grow window to the right, grow main pane (monadtall), grow window (monadwide)"),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(), grow_monad(direction="down"),
        desc="Grow window down, shrink window (monadtall), grow main pane (monadwide)"),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(), grow_monad(direction="up"),
        desc="Grow window up, grow window (monadtall), shrink main pane (monadwide)"),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(), grow_monad(direction="left"),
        desc="Grow window to the left, shrink main pane (monadtall), shrink window (monadwide)"),
    Key([mod, "control"], "l",
        lazy.layout.grow_right(), grow_monad(direction="right"),
        desc="Grow window to the right, grow main pane (monadtall), grow window (monadwide)"),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(), grow_monad(direction="down"),
        desc="Grow window down, shrink window (monadtall), grow main pane (monadwide)"),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(), grow_monad(direction="up"),
        desc="Grow window up, grow window (monadtall), shrink main pane (monadwide)"),
    Key([mod], "n",
        lazy.layout.normalize(),
        desc="Reset all window sizes"),
    Key([mod, "control"], "n",
        lazy.layout.reset(),
        desc="Reset all window sizes (including primary)"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod], "s",
        lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

    Key([mod], "t",
        lazy.spawn(terminal),
        desc="Launch terminal"),
    Key([mod], "Tab", 
        lazy.next_layout(),
        desc="Toggle between layouts"),
    Key([mod], "x",
        lazy.window.kill(),
        desc="Kill focused window"),
    Key([mod, "control"], "r",
        lazy.reload_config(),
        desc="Reload the config"),
    Key([mod, "control"], "q",
        lazy.shutdown(),
        desc="Shutdown Qtile"),
    Key([mod], "Return",
        lazy.spawn("rofi -show drun"),
        desc="Bring up rofi"),
    Key([mod, "shift"], "Return",
        lazy.spawn("rofi -show p -modi p:rofi-powermenu"),
        desc="Bring up rofi-powermenu"),
    Key([mod], "m",
        lazy.window.toggle_maximize(),
        desc="Toggle maximize"),
    Key([mod, "shift"], "m",
        lazy.window.toggle_minimize(),
        desc="Toggle minimize"),

    Key(
        [], "XF86AudioRaiseVolume",
        lazy.spawn("amixer set Master 10%+")
        #lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +10%")
    ),
    Key(
        [], "XF86AudioLowerVolume",
        lazy.spawn("amixer set Master 10%-")
        #lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -10%")
    ),
    Key(
        [], "XF86AudioMute",
        lazy.spawn("amixer set Master toggle")
        #lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")
    ),
]

groups = [Group(i) for i in "12345"]

for i in groups:
    keys.extend(
        [   # mod1 + letter of group = switch to group
            Key([mod], i.name,
                lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),

            # mod1 + shift + letter of group = switch to & move focused window to group
            Key([mod, "shift"], i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name)),

            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

def init_layout_theme():
    return { "margin": 4,
             "border_width": 3,
             "border_focus": nord[8],
             "border_normal": nord[10]
           }

layout_theme = init_layout_theme()

layouts = [
    layout.MonadTall(align=layout.MonadTall._left, **layout_theme),
    layout.MonadWide(align=layout.MonadTall._left, **layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme),
    layout.TreeTab()
    # layout.Columns(**layout_theme),
    # layout.Floating(),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Kanit",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_method="block",
                    this_current_screen_border=nord[9],
                    inactive="#ffffff",
                    padding_y = 1
                ),
                widget.Spacer(),
                widget.WindowName(
                    width=700,
                    max_chars=100
                ),
                widget.Spacer(),
                widget.CurrentLayout(
                    fmt="  {}",
                    background=nord[11],
                    foreground=nord[1],
                    padding=6
                ),
                widget.CheckUpdates(
                    distro="Arch_checkupdates",
                    update_interval=1800,
                    display_format="  {updates}",
                    no_update_string="  0",
                    background=nord[12],
                    foreground=nord[1],
                    colour_have_updates=nord[1],
                    colour_no_updates=nord[1],
                    padding=6
                ),
                widget.Volume(
                    fmt="墳  {}",
                    background=nord[13],
                    foreground=nord[1],
                    padding=6
                ),
               # Widget to control volume with pactl (goes over 100)
               # Volume(
               #         fmt = " {}",
               #         background=nord[13],
               #         foreground=nord[1],
               #         padding=6,
               #         get_volume_command = "pactl get-sink-volume @DEFAULT_SINK@",
               #         check_mute_command = "pactl get-sink-mute @DEFAULT_SINK@",
               #         check_mute_string = "yes",
               #         volume_up_command = "pactl set-sink-volume @DEFAULT_SINK@ +2%",
               #         volume_down_command = "pactl set-sink-volume @DEFAULT_SINK@ -2%",
               #         mute_command = "pactl set-sink-mute @DEFAULT_SINK@ toggle",
               #  ),
                widget.Net(
                    format='{up}   {down}',
                    interface='enp1s0',
                    background=nord[14],
                    foreground=nord[1],
                    padding=6
                ),
                widget.Clock(
                    fmt="  {}",
                    format="%d/%m/%y %a %H:%M",
                    background=nord[15],
                    foreground=nord[1],
                    padding=6
                ),
                widget.TextBox(
                    text='',
                    mouse_callbacks= {
                        'Button1': lazy.spawn(
                        "rofi -show p -modi p:rofi-powermenu")
                    },
                    background=nord[3],
                    padding=10
                )
            ],
            26,
            background="#00000000"
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_width=2,
    border_focus="#a3be8c",
    border_normal="#d8dee9"
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
follow_mouse_focus = False

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
