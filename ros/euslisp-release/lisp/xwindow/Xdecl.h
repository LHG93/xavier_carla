static pointer (*ftab[4])();

#define QUOTE_STRINGS_SIZE 189
static char *quote_strings[QUOTE_STRINGS_SIZE]={
    ":long",
    ":integer",
    "\"X\"",
    "\"X\"",
    "*package*",
    "\"no such package\"",
    "(xobject xcolor colormap gcontext xdrawable xpixmap xwindow)",
    "(panel-item button-item menu-button-item slider-item joystick-item text-item choice-item)",
    "(xscroll-bar xhorizontal-scroll-bar)",
    "(canvas graph-canvas characterwindow textwindow textwindowstream buffertextwindow scrolltextwindow)",
    "(panel menu-panel)",
    "(filedialog filepanel textviewpanel confirmpanel eustop-win)",
    "(menubar-panel bitmap-button-item)",
    "(*display* *xwindows* *xwindows-hash-tab* *visual* *visuals* *visual-pseudo-8* *visual-true-8* *visual-direct-8* *visual-true-15* *visual-direct-15* *visual-true-16* *visual-direct-16* *visual-true-24* *visual-direct-24* *root* *screen* *screen-no* *depth* *blackpixel* *whitepixel* *fg-pixel* *bg-pixel* *whitegc* *blackgc* *defaultgc* *gray25-pixmap* *gray50-pixmap* *gray75-pixmap* *gray25-bitmap* *gray50-bitmap* *gray75-bitmap* *gray25-gc* *gray50-gc* *gray75-gc* *eustop-win* *shell-window* init-xwindow make-pixmaps make-cleared-pixmap make-default-cmap make-color-gc make-xwindow find-xwindow)",
    "(font-cour8 font-cour10 font-cour12 font-cour14 font-cour18 font-courb12 font-courb14 font-courb18 font-courb24 font-timesb12 font-timesb14 font-timesb18 font-timesb24 font-times10 font-times12 font-lucidasans-bold-12 font-lucidasans-bold-14 font-helvetica-bold-12 font-helvetica-12 font-a14)",
    "*display*",
    ":vtype",
    ":global",
    "*visual*",
    "*visual-pseudo-8*",
    "*visual-true-8*",
    "*visual-direct-8*",
    "*visual-true-15*",
    "*visual-direct-15*",
    "*visual-true-16*",
    "*visual-direct-16*",
    "*visual-true-24*",
    "*visual-direct-24*",
    "*root*",
    "*screen*",
    "*screen-no*",
    "*blackpixel*",
    "*whitepixel*",
    "*whitegc*",
    "*blackgc*",
    "*defaultgc*",
    "*fg-pixel*",
    "*bg-pixel*",
    "*gray25-pixmap*",
    "*gray50-pixmap*",
    "*gray75-pixmap*",
    "*gray25-gc*",
    "*gray50-gc*",
    "*gray75-gc*",
    "*color-map*",
    "*xwindows*",
    "*xwindows-hash-tab*",
    ":size",
    "make-hash-table",
    "*visuals*",
    "font-cour8",
    "font-cour10",
    "font-cour12",
    "font-cour14",
    "font-cour18",
    "font-courb12",
    "font-courb14",
    "font-courb18",
    "font-courb24",
    "font-lucidasans-bold-12",
    "font-lucidasans-bold-14",
    "font-helvetica-bold-12",
    "font-helvetica-12",
    "font-a14",
    "font-times10",
    "font-times12",
    "font-timesb12",
    "font-timesb14",
    "font-timesb18",
    "font-timesb24",
    "*save-under*",
    "*depth*",
    "*default-ximage*",
    "*gray-gc*",
    "*gray-pixmap*",
    "xobject",
    ":super",
    "geometry:viewsurface",
    ":slots",
    "(display)",
    ":metaclass",
    ":element-type",
    ":documentation",
    "make-class",
    "colormap",
    "propertied-object",
    "(cmapid planes pixels lut-list)",
    "gcontext",
    "(gcid gcvalues)",
    "xdrawable",
    "(drawable (gcon :forward t) bg-color width height)",
    "xpixmap",
    "nil",
    "xwindow",
    "(parent subwindows visual backing-pixmap event-forward)",
    "panel",
    "(pos items fontid rows columns next-x next-y item-width item-height dark-edge-color light-edge-color topleft-edge-polygon active-menu)",
    "canvas",
    "(topleft bottomright buttonactive menu)",
    "panel-item",
    "(pos notify-object notify-method fontid label labeldots buttonpressed)",
    "button-item",
    "(submenu activecolor 3d-state dark-edge-color light-edge-color topleft-edge-polygon)",
    "text-item",
    "(textwin)",
    "slider-item",
    "(min-value max-value value minlabel maxlabel valueformat bar-x bar-y bar-width bar-height valuedots label-base nob-x nob-moving charwidth continuous-notify)",
    "menu-button-item",
    "(items item-dots item-labels charwidth charheight menu-window window-pos high-light)",
    "choice-item",
    "(choice-list active-choice transient-choice choice-pos button-size)",
    "joystick-item",
    "(stick-size min-x min-y max-x max-y center-x center-y stick-x stick-y value-x value-y stick-return stick-grabbed fraction-x fraction-y follow-move)",
    "menu-panel",
    "(height-offset menu-buttons)",
    "xscroll-bar",
    "(arrow-length handle-pos handle-length verticalp handle-grabbed)",
    "xhorizontal-scroll-bar",
    "characterwindow",
    "(fontid charwidth charheight charascent win-row-max win-col-max x y)",
    "textwindow",
    "(win-row win-col charbuf keybuf keycount echo show-cursor cursor-on notify-object notify-method buttonactive)",
    "buffertextwindow",
    "(linebuf expbuf max-line-length selected-pos)",
    "scrolltextwindow",
    "(row col top-row top-col scroll-bar-window horizontal-scroll-bar-window selected-line)",
    "textwindowstream",
    "stream",
    "(textwin)",
    "menubar-panel",
    "bitmap-button-item",
    "(pixmap-id bitmap-width bitmap-height)",
    "noeventmask",
    ":constant",
    "keypressmask",
    "keyreleasemask",
    "buttonpressmask",
    "buttonreleasemask",
    "enterwindowmask",
    "leavewindowmask",
    "pointermotionmask",
    "pointermotionhintmask",
    "button1motionmask",
    "button2motionmask",
    "button3motionmask",
    "button4motionmask",
    "button5motionmask",
    "buttonmotionmask",
    "keymapstatemask",
    "exposuremask",
    "visibilitychangemask",
    "structurenotifymask",
    "resizeredirectmask",
    "substructurenotifymask",
    "substructureredirectmask",
    "focuschangemask",
    "propertychangemask",
    "colormapchangemask",
    "ownergrabbuttonmask",
    "c-long",
    "carray",
    "cstructclass",
    ":byte",
    ":slotlist",
    "((#:long77 :long 1))",
    "c-long-long77",
    "\"(lisp::s lisp::i)\"",
    "set-c-long-long77",
    "lisp::setf-update-fn",
    "lisp::setf-lambda",
    "remprop",
    "lisp::setf-method",
    "lisp::setf-documentation",
    "\"(lisp::s lisp::i lisp::val)\"",
    "\"(lisp::s &optional (lisp::i 0))\"",
    "set-c-long",
    "\"(lisp::s lisp::i &optional lisp::val)\"",
    "c-int",
    "((#:integer90 :integer 1))",
    "c-int-integer90",
    "\"(lisp::s lisp::i)\"",
    "set-c-int-integer90",
    "\"(lisp::s lisp::i lisp::val)\"",
    "\"(lisp::s &optional (lisp::i 0))\"",
    "set-c-int",
    "\"(lisp::s lisp::i &optional lisp::val)\"",
    ":xdecl",
    "\"@(#)$Id: Xdecl.l,v 1.1.1.1 2003/11/20 07:46:34 eus Exp $\"",
    "provide",
  };
