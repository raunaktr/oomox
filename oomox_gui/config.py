import os


script_dir = os.path.dirname(os.path.realpath(__file__))
gtk_preview_css_dir = os.path.join(script_dir, "gtk_preview_css/")
terminal_template_dir = os.path.join(script_dir, "terminal_templates/")

oomox_root_dir = os.path.join(script_dir, "../")
colors_dir = os.path.join(oomox_root_dir, "colors/")
plugins_dir = os.path.join(oomox_root_dir, "plugins/")
gtk_theme_dir = os.path.join(oomox_root_dir, "gtk-theme/")
archdroid_theme_dir = os.path.join(oomox_root_dir, "archdroid-icon-theme/")
gnome_colors_icon_theme_dir = os.path.join(oomox_root_dir, "gnome-colors-icon-theme/")
oomoxify_script_path = os.path.join(oomox_root_dir, "oomoxify/oomoxify.sh")

user_config_dir = os.path.join(
    os.environ.get(
        "XDG_CONFIG_HOME",
        os.path.join(os.environ.get("HOME"), ".config/")
    ),
    "oomox/"
)
user_theme_dir = os.path.join(user_config_dir, "colors/")
user_plugins_dir = os.path.join(user_config_dir, "plugins/")
user_palette_path = os.path.join(user_config_dir, "recent_palette.json")
user_export_config_dir = os.path.join(user_config_dir, "export_config/")

FALLBACK_COLOR = "F33333"
