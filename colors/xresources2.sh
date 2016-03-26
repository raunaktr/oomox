get_color () {
	xrdb -query | grep "$1:" | cut -f2 | sed -r 's/#//' | head -n 1
}
color () {
	get_color color$1
}
color_bg () {
	get_color "*background"
}
color_fg () {
	get_color "*foreground"
}

   NAME="follow xresources theme"
     BG=$(color 7)
     FG=$(color 0)
 TXT_BG=$(color_fg)
 TXT_FG=$(color 0)
 SEL_BG=$(color 1)
 SEL_FG=$TXT_BG
MENU_BG=$(color_bg)
MENU_FG=$BG
 BTN_BG=$(color 12)
 BTN_FG=$(color 0)
