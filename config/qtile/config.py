import os
import subprocess

from libqtile import hook

from libqtile.extension.dmenu import DmenuRun
from libqtile.bar import Bar, CALCULATED

# import layout objects
from libqtile.layout.columns import Columns 
from libqtile.layout.max import Max
from libqtile.layout.floating import Floating

# import widgets and bar
from libqtile.widget.base import _TextBox
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.window_count import WindowCount
from libqtile.widget.windowname import WindowName
from libqtile.widget.cpu import CPU
from libqtile.widget.memory import Memory
from libqtile.widget.systray import Systray
from libqtile.widget.clock import Clock
from libqtile.widget.spacer import Spacer
from libqtile.widget.textbox import TextBox

from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from colors import gruvbox


mod = "mod4"
#terminal = guess_terminal()
terminal = 'alacritty'

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "control"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "control"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "control"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "control"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "shift"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "shift"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "shift"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "shift"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "s", lazy.spawn("alacritty -e alsamixer"), desc="Volumn setting"),
    Key([mod, "control"], "d", lazy.spawn('alacritty -e rm -rf ~/.local/share/nvim/swap/*'), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.window.toggle_floating(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key(
        [mod],
        "e",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key(
        [mod],
        "Escape",
        #lazy.spawn("i3lock --blur 4 --screen 1 --clock --inside-color '#002b36' --date-color '#ffffff' --time-color '#ffffff' --wrong-text 'Auth Failed' --verif-text 'Verifying...' --wrong-color '#ffffff' --verif-color '#ffffff'"),
        lazy.spawn("alacritty -e betterlockscreen -l blur"),
        desc="lock screen",
    ),
    Key([mod], "t", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "Escape", lazy.shutdown(), desc="Shutdown Qtile"),
#Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Spawn a command using a prompt widget"),
    # DmenuRun
    Key([mod], 'r', lazy.run_extension(DmenuRun(
        font="TerminessTTF Nerd Font",
        fontsize="13",
        dmenu_command="dmenu_run",
        dmenu_prompt=" ",
        #dmenu_height=10,
        dmenu_lines=15,
        background=gruvbox['bg'],
        foreground=gruvbox['gray'],
        selected_foreground=gruvbox['blue-alt'],
        selected_background=gruvbox['bg'],
    ))),
     ### Switch focus to specific monitor (out of three)
    #Key([mod], "w",
    #    lazy.to_screen(0),
    #    desc='Keyboard focus to monitor 1'
    #    ),
    #Key([mod], "e",
    #    lazy.to_screen(1),
    #    desc='Keyboard focus to monitor 2'
    #    ),
    #Key([mod], "r",
    #    lazy.to_screen(2),
    #    desc='Keyboard focus to monitor 3'
    #    ),
    ### Switch focus of monitors
    Key([mod], "Tab",
        lazy.next_screen(),
        desc='Move focus to next monitor'
        ),
    Key([mod, "shift"], "Tab",
        lazy.prev_screen(),
        desc='Move focus to prev monitor'
        ),
]

#groups = [Group(i) for i in "123456789"]
groups = [
    Group('1', label='一', layout='columns'),
    Group('2', label='二', matches=[Match(wm_class='Brave-browser')], layout='columns'),
    Group('3', label='三', matches=[Match(wm_class='Microsoft Teams - Preview'), Match(wm_class='TelegramDesktop')], layout='columns'),
    Group('4', label='四', matches=[Match(wm_class='Google-chrome')], layout='columns'),
    Group('5', label='五', matches=[Match(wm_class='')], layout='columns'),
    Group('6', label='六', matches=[Match(wm_class='')], layout='columns'),
    Group('7', label='七', matches=[Match(wm_class='')], layout='columns'),
    Group('8', label='八', matches=[Match(wm_class='firefox')], layout='columns'),
    Group('9', label='九', matches=[Match(wm_class='obs')], layout='columns'),
    Group('0', label='零', matches=[Match(wm_class='Org.gnome.clocks')], layout='columns'),
]

#prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
           Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    Columns(
        border_normal=gruvbox['gray'],
        border_focus_stack="#d75f5f",
        border_width=2,
        border_normal_stack=gruvbox['gray'],
        border_focus='#98971a',
        border_on_single=2,
        margin=5,
        margin_on_single=5,
    ),
    Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Fira Code Bold",
    fontsize=12,
    padding=10,
    foreground=gruvbox['bg']
)
extension_defaults = widget_defaults.copy()

class MyCustomWidget(_TextBox):
    defaults = [
            ("font", "sans", "Text font"),
            ("fontsize", None, "Font pixel size. Calculated if None."),
            ("fontshadow", None, "font shadow color, default is None(no shadow)"),
            ("padding", None, "Padding left and right. Calculated if None."),
            ("foreground", "#ffffff", "Foreground colour."),
    ]  

    def __init__(self, text=" ", width=CALCULATED, **config):
        _TextBox.__init__(self, text=text, width=width, **config)

    def cmd_update(self, text):
        """Update the text in a TextBox widget"""
        self.update(text=text)

    def cmd_get(self):
        """Retrieve the text in a TextBox widget"""
        return self.text

screens = [
          Screen(
              top=Bar(
                  [
                      Spacer(length=10),
                      CurrentLayout(
                          background=gruvbox['blue-alt'],
                      ),
                      Spacer(length=10),

                      WindowCount(
                          text_format=' {num}',
                          background=gruvbox['green'],
                          show_zero=True
                      ),

                      Spacer(length=10),

                      # Prompt(foreground=gruvbox['fg']),

                      GroupBox(
                          disable_drag=True,
                          active=gruvbox['fg'],
                          inactive=gruvbox['gray-alt'],
                          highlight_method='line',
                          block_highlight_text_color=gruvbox['red-alt'],
                          this_screen_border=gruvbox['purple-alt'],
                          this_current_screen_border=gruvbox['green'],
                          borderwidth=2,
                          highlight_color=gruvbox['bg'],
                          background=gruvbox['bg']
                      ),

                      WindowName(foreground=gruvbox['fg']),


                      Spacer(length=100),
                      Systray(),

                      Spacer(length=10),

                      CPU(
                          format=' {freq_current}GHz {load_percent}%',
                          background=gruvbox['blue']),

                      Spacer(length=10),

                      Memory(
                          format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
                          background=gruvbox['red-alt']),

                      Spacer(length=10),

                      Clock(
                          background=gruvbox['orange'],
                          format=' %Y-%m-%d %a %I:%M %p'),

                      Spacer(length=10),
                  ],
                  margin=[10, 10, 5, 10],
                  background='#24352100',
                  opacity=1,
                  size=25,
              ),
          ),
          Screen(
              top=Bar(
                  [
                      Spacer(length=10),
                      CurrentLayout(
                          background=gruvbox['blue-alt'],
                      ),
                      Spacer(length=10),

                      WindowCount(
                          text_format=' {num}',
                          background=gruvbox['green'],
                          show_zero=True
                      ),

                      Spacer(length=10),

                      # Prompt(foreground=gruvbox['fg']),


                      GroupBox(
                          disable_drag=True,
                          active=gruvbox['fg'],
                          inactive=gruvbox['gray-alt'],
                          highlight_method='line',
                          block_highlight_text_color=gruvbox['red-alt'],
                          this_screen_border=gruvbox['purple-alt'],
                          this_current_screen_border=gruvbox['green'],
                          borderwidth=2,
                          highlight_color=gruvbox['bg'],
                          background=gruvbox['bg']
                      ),

                      WindowName(foreground=gruvbox['fg']),

                      Spacer(length=100),
                      
                      #TextBox(text="Working mode", background=gruvbox['yellow']),
                      MyCustomWidget(text="Working mode", background=gruvbox['yellow'], mouse_callbacks={'Button1': lazy.spawn('alacritty')}),

                      Spacer(length=10),

                      CPU(
                          format=' {freq_current}GHz {load_percent}%',
                          background=gruvbox['blue']),

                      Spacer(length=10),

                      Memory(
                          format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
                          background=gruvbox['orange-alt']),

                      Spacer(length=10),

                      Clock(
                          background=gruvbox['aqua'],
                          format=' %Y-%m-%d %a %I:%M %p'),

                      Spacer(length=10),
                  ],
                  margin=[10, 10, 5, 10],
                  background='#00000000',
                  opacity=1,
                  size=25,
              ),
          )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False

floating_layout = Floating(
    border_normal=gruvbox['gray-alt'],
    border_focus=gruvbox['yellow-alt'],
    border_width=4,
    float_rules=[
        *Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
        Match(wm_class="pavucontrol"),
        Match(wm_class="zoom"),
        Match(wm_class="bitwarden"),
        Match(wm_class="kdenlive"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])

@hook.subscribe.startup_once
def start_once():
    #    lazy.spawn("alacritty")
    #    lazy.spawn("/usr/bin/teams")
    #    lazy.spawn("/usr/bin/telegram")
    home = os.path.expanduser('~/.config/qtile/autostart_once.sh')
    subprocess.run([home])

autostart()
#start_once()

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D" 
