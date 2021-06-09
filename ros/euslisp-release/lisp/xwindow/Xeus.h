static pointer FLET750();
static pointer CLO1028();
static pointer (*ftab[68])();

#define QUOTE_STRINGS_SIZE 528
static char *quote_strings[QUOTE_STRINGS_SIZE]={
    ":long",
    ":integer",
    "gcontext",
    ":create",
    ":drawable",
    "*xwindows-hash-tab*",
    "sethash",
    "*display*",
    "flush",
    "c-long",
    "c-int",
    "getgeometry",
    ":geometry",
    "wa",
    "getwindowattributes",
    ":get",
    "x",
    "y",
    "send",
    ":gc",
    ":line-width",
    ":line-style",
    ":foreground",
    "#(:width :height :source-x :source-y :x :y)",
    "copyarea",
    ":width",
    ":height",
    "drawpoint",
    "drawline",
    "drawrectangle",
    "rad2deg",
    "drawarc",
    "fillrectangle",
    "fillarc",
    "drawstring",
    "drawimagestring",
    "#(:xy :x :y :width :height :mask :format)",
    "getimage",
    "make-string",
    "make-foreign-string",
    ":start1",
    ":end1",
    "replace",
    "destroyimage",
    "#(:src :src-x :src-y :dst :dst-x :dst-y :width :height :gc :visual :depth :bitunit :ximage)",
    ":visual",
    "visual-depth",
    "*default-ximage*",
    "image::image-2d",
    "set-ximage",
    "putimage",
    "#(:src :src-x :src-y :dst :dst-x :dst-y :width :height :gc :&aux :image32 :pixel8)",
    ":element-type",
    "make-array",
    ":point",
    ":line",
    ":string",
    ":image-string",
    ":rectangle",
    ":fill-rectangle",
    ":arc",
    ":fill-arc",
    ":function",
    ":copy",
    ":clear",
    ":xor",
    "#(:x :y :width :height :gc)",
    ":clear-area",
    "#(:color :max :min :gc :clear :step)",
    "cons",
    "max",
    "min",
    ":flat",
    ":up",
    ":down",
    ":fill-polygon",
    "#(:size :width :height :depth :gc)",
    "defaultdepth",
    "*defaultgc*",
    "defaultrootwindow",
    "createpixmap",
    ":init",
    "super",
    "readbitmapfile",
    "writebitmapfile",
    "freepixmap",
    "#(:size :width :height :gc)",
    "*blackgc*",
    "xpixmap",
    "#(:foreground :background :depth)",
    "*fg-pixel*",
    "*bg-pixel*",
    "bit-vector",
    "(18 22 0 4 2 6 16 20 9 13 27 31 25 29 11 15 8 12 26 30 24 28 10 14 1 5 19 23 17 21 3 7)",
    "*root*",
    "createpixmapfrombitmapdata",
    "#(:foreground :background :depth)",
    ":change-attributes",
    ":fill-style",
    ":background",
    ":depth",
    ":tile",
    "((:keypress 1) (:keyrelease 2) (:key 3) (:button 12) (:buttonpress 4) (:buttonrelease 8) (:enterleave 48) (:enterwindow 16) (:leavewindow 32) (:pointermotion 64) (:pointermotionhint 128) (:buttonmotion 8192) (:motion 8192) (:keymapstate 16384) (:exposure 32768) (:visibilitychange 65536) (:configure 131072) (:structurenotify 131072) (:resizeredirect 262144) (:substructurenotify 524288) (:substructureredirect 1048576) (:focuschange 2097152) (:propertychage 4194304) (:colormapchage 8388608) (:ownergrabbutton 16777216))",
    "assoc",
    "\"unknown event-mask keyword ~s~%\"",
    "warn",
    "((:forget . 0) (:northwest . 1) (:north . 2) (:northeast . 3) (:west . 4) (:center . 5) (:east . 6) (:southwest . 7) (:south . 8) (:southeast . 9) (:static . 10))",
    "\"invalid gravity name\"",
    "#(:parent :x :y :size :width :height :border-width :border :save-under :backing-store :backing-pixmap :foreground :background :title :event-mask :gc :font :name :map :visual :depth :color-map :override-redirect :gravity)",
    ":always",
    "\"WINDOW\"",
    "string",
    "*visual*",
    ":northwest",
    "*save-under*",
    "((:notuseful 0) (:whenmapped 1) (:always 2))",
    "(:exposure :visibilitychange)",
    "swa",
    ":colormap",
    "colormap",
    ":copy-colors",
    "*color-map*",
    ":id",
    "createwindow",
    "storename",
    ":get-pixel",
    "\"cannot :get-pixel for ~a~%\"",
    "setwindowbackground",
    "clearwindow",
    "mapwindow",
    ":associate",
    "*xwindows*",
    ":font",
    ":name",
    ":map",
    "send-all",
    ":unmap",
    "unmapwindow",
    ":test",
    ":test-not",
    ":key",
    "member",
    "delete",
    "reparentwindow",
    ":destroy",
    "destroywindow",
    ":dissociate",
    "remhash",
    "windowattributes",
    ":attributes",
    "your_event_mask",
    "selectinput",
    "visual",
    "width",
    "height",
    "depth",
    "screen",
    "gethash",
    "\"~s's parent ~s does not have cmap; root cmap is used.~%\"",
    "warning-message",
    "root",
    "setwindowbackgroundpixmap",
    "setwindowborder",
    ":copy-from",
    "movewindow",
    "resizewindow",
    "raisewindow",
    "lowerwindow",
    ":write-to-bitmap-file",
    "#(:x :y :width :height)",
    "cleararea",
    "cmapid",
    "setwindowcolormap",
    "xwindow",
    ":set",
    ":short",
    "drawlines",
    ":draw-lines",
    "fillpolygon",
    "changewindowattributes",
    "settransientforhint",
    "querypointer",
    ":querypointer",
    "substringp",
    ":geoclasses",
    "\"geo/geoclasses.l\"",
    "require",
    ":xdecl",
    "\"Xdecl.l\"",
    "\"X\"",
    "\"X\"",
    "*package*",
    "\"no such package\"",
    ":vtype",
    ":global",
    "(*save-under*)",
    "setwindowattributes",
    ":super",
    "cstruct",
    ":slots",
    "nil",
    ":metaclass",
    "cstructclass",
    ":byte",
    ":size",
    ":documentation",
    "make-class",
    ":slotlist",
    "((pixmap :long) (background_pixel :long) (border_pixmap :long) (border_pixel :long) (bit_gravity :integer) (win_gravity :integer) (backing_store :integer) (backing_planes :long) (backing_pixel :long) (save_under :integer) (event_mask :long) (do_not_propagate_mask :long) (override_redirect :integer) (colormap :long) (cursor :long))",
    "setwindowattributes-pixmap",
    "\"(lisp::s)\"",
    "set-setwindowattributes-pixmap",
    "lisp::setf-update-fn",
    "lisp::setf-lambda",
    "remprop",
    "lisp::setf-method",
    "lisp::setf-documentation",
    "\"(lisp::s lisp::val)\"",
    "setwindowattributes-background_pixel",
    "\"(lisp::s)\"",
    "set-setwindowattributes-background_pixel",
    "\"(lisp::s lisp::val)\"",
    "setwindowattributes-border_pixmap",
    "\"(lisp::s)\"",
    "set-setwindowattributes-border_pixmap",
    "\"(lisp::s lisp::val)\"",
    "setwindowattributes-border_pixel",
    "\"(lisp::s)\"",
    "set-setwindowattributes-border_pixel",
    "\"(lisp::s lisp::val)\"",
    "setwindowattributes-bit_gravity",
    "\"(lisp::s)\"",
    "set-setwindowattributes-bit_gravity",
    "\"(lisp::s lisp::val)\"",
    "setwindowattributes-win_gravity",
    "\"(lisp::s)\"",
    "set-setwindowattributes-win_gravity",
    "\"(lisp::s lisp::val)\"",
    "setwindowattributes-backing_store",
    "\"(lisp::s)\"",
    "set-setwindowattributes-backing_store",
    "\"(lisp::s lisp::val)\"",
    "setwindowattributes-backing_planes",
    "\"(lisp::s)\"",
    "set-setwindowattributes-backing_planes",
    "\"(lisp::s lisp::val)\"",
    "setwindowattributes-backing_pixel",
    "\"(lisp::s)\"",
    "set-setwindowattributes-backing_pixel",
    "\"(lisp::s lisp::val)\"",
    "setwindowattributes-save_under",
    "\"(lisp::s)\"",
    "set-setwindowattributes-save_under",
    "\"(lisp::s lisp::val)\"",
    "setwindowattributes-event_mask",
    "\"(lisp::s)\"",
    "set-setwindowattributes-event_mask",
    "\"(lisp::s lisp::val)\"",
    "setwindowattributes-do_not_propagate_mask",
    "\"(lisp::s)\"",
    "set-setwindowattributes-do_not_propagate_mask",
    "\"(lisp::s lisp::val)\"",
    "setwindowattributes-override_redirect",
    "\"(lisp::s)\"",
    "set-setwindowattributes-override_redirect",
    "\"(lisp::s lisp::val)\"",
    "setwindowattributes-colormap",
    "\"(lisp::s)\"",
    "set-setwindowattributes-colormap",
    "\"(lisp::s lisp::val)\"",
    "setwindowattributes-cursor",
    "\"(lisp::s)\"",
    "set-setwindowattributes-cursor",
    "\"(lisp::s lisp::val)\"",
    "((x :integer) (y :integer) (width :integer) (height :integer) (border_width :integer) (depth :integer) (visual :long) (root :long) (class :integer) (bit_gravity :integer) (win_gravity :integer) (backing_store :integer) (backing_planes :long) (backing_pixel :long) (save_under :integer) (colormap :long) (map_installed :integer) (map_state :integer) (all_event_masks :long) (your_event_mask :long) (do_not_propagate_mask :long) (override_redirect :integer) (screen :long))",
    "windowattributes-x",
    "\"(lisp::s)\"",
    "set-windowattributes-x",
    "\"(lisp::s lisp::val)\"",
    "windowattributes-y",
    "\"(lisp::s)\"",
    "set-windowattributes-y",
    "\"(lisp::s lisp::val)\"",
    "windowattributes-width",
    "\"(lisp::s)\"",
    "set-windowattributes-width",
    "\"(lisp::s lisp::val)\"",
    "windowattributes-height",
    "\"(lisp::s)\"",
    "set-windowattributes-height",
    "\"(lisp::s lisp::val)\"",
    "windowattributes-border_width",
    "\"(lisp::s)\"",
    "set-windowattributes-border_width",
    "\"(lisp::s lisp::val)\"",
    "windowattributes-depth",
    "\"(lisp::s)\"",
    "set-windowattributes-depth",
    "\"(lisp::s lisp::val)\"",
    "windowattributes-visual",
    "\"(lisp::s)\"",
    "set-windowattributes-visual",
    "\"(lisp::s lisp::val)\"",
    "windowattributes-root",
    "\"(lisp::s)\"",
    "set-windowattributes-root",
    "\"(lisp::s lisp::val)\"",
    "windowattributes-class",
    "\"(lisp::s)\"",
    "set-windowattributes-class",
    "\"(lisp::s lisp::val)\"",
    "windowattributes-bit_gravity",
    "\"(lisp::s)\"",
    "set-windowattributes-bit_gravity",
    "\"(lisp::s lisp::val)\"",
    "windowattributes-win_gravity",
    "\"(lisp::s)\"",
    "set-windowattributes-win_gravity",
    "\"(lisp::s lisp::val)\"",
    "windowattributes-backing_store",
    "\"(lisp::s)\"",
    "set-windowattributes-backing_store",
    "\"(lisp::s lisp::val)\"",
    "windowattributes-backing_planes",
    "\"(lisp::s)\"",
    "set-windowattributes-backing_planes",
    "\"(lisp::s lisp::val)\"",
    "windowattributes-backing_pixel",
    "\"(lisp::s)\"",
    "set-windowattributes-backing_pixel",
    "\"(lisp::s lisp::val)\"",
    "windowattributes-save_under",
    "\"(lisp::s)\"",
    "set-windowattributes-save_under",
    "\"(lisp::s lisp::val)\"",
    "windowattributes-colormap",
    "\"(lisp::s)\"",
    "set-windowattributes-colormap",
    "\"(lisp::s lisp::val)\"",
    "windowattributes-map_installed",
    "\"(lisp::s)\"",
    "set-windowattributes-map_installed",
    "\"(lisp::s lisp::val)\"",
    "windowattributes-map_state",
    "\"(lisp::s)\"",
    "set-windowattributes-map_state",
    "\"(lisp::s lisp::val)\"",
    "windowattributes-all_event_masks",
    "\"(lisp::s)\"",
    "set-windowattributes-all_event_masks",
    "\"(lisp::s lisp::val)\"",
    "windowattributes-your_event_mask",
    "\"(lisp::s)\"",
    "set-windowattributes-your_event_mask",
    "\"(lisp::s lisp::val)\"",
    "windowattributes-do_not_propagate_mask",
    "\"(lisp::s)\"",
    "set-windowattributes-do_not_propagate_mask",
    "\"(lisp::s lisp::val)\"",
    "windowattributes-override_redirect",
    "\"(lisp::s)\"",
    "set-windowattributes-override_redirect",
    "\"(lisp::s lisp::val)\"",
    "windowattributes-screen",
    "\"(lisp::s)\"",
    "set-windowattributes-screen",
    "\"(lisp::s lisp::val)\"",
    "xdrawable",
    "\"(self class id &optional w h system:gc)\"",
    "\"(self class)\"",
    ":flush",
    "\"(self class)\"",
    "\"(self class)\"",
    "\"(self class)\"",
    "\"(self class)\"",
    ":pos",
    "\"(self class)\"",
    ":x",
    "\"(self class)\"",
    ":y",
    "\"(self class)\"",
    "\"(self class &rest newgc)\"",
    ":gcid",
    "\"(self class)\"",
    "\"(self class &optional dots)\"",
    "\"(self class &optional dash)\"",
    ":color",
    "\"(self class &optional color)\"",
    "\"(self class dw &key (width) (height) (source-x 0) (source-y 0) (x 0) (y 0))\"",
    ":shift",
    "\"(self class x &optional (y 0))\"",
    "\"(self class x y &optional (system:gc gcon))\"",
    "\"(self class x1 y1 x2 y2 &optional (system:gc gcon))\"",
    "\"(self class x y width height &optional (system:gc gcon))\"",
    "\"(self class x y width &optional (height width) (angle1 0.0) (angle2 2pi) (system:gc gcon))\"",
    "\"(self class x y width height &optional (system:gc gcon))\"",
    "\"(self class x y width &optional (height width) (angle1 0.0) (angle2 2pi) (system:gc gcon))\"",
    "\"(self class x y str &optional (start 0) (end (length str)) (system:gc gcon))\"",
    "\"(self class x y str &optional (start 0) (end (length str)) (system:gc gcon))\"",
    ":getimage",
    "\"(self class &key (xy nil) (x 0) (y 0) (width (- (send self :width) x)) (height (- (send self :height) y)) (mask 1152921504606846975) (format 2))\"",
    ":putimage",
    "\"(self class image &key (src nil) (src-x 0) (src-y 0) (dst nil) (dst-x 0) (dst-y 0) (width) (height) ((:gc g) gcon) (visual (send self :visual)) (depth (visual-depth visual)) (bitunit depth) (ximage *default-ximage*))\"",
    ":putimage8to24",
    "\"(self class image &key (src nil) (src-x 0) (src-y 0) (dst nil) (dst-x 0) (dst-y 0) (width (- (send self :width) dst-x)) (height (- (send self :height) dst-y)) ((:gc g) gcon) &aux image32 pixel8)\"",
    ":draw-point",
    "\"(self class p &optional (system:gc gcon))\"",
    ":draw-line",
    "\"(self class from to &optional (system:gc gcon))\"",
    ":draw-string",
    "\"(self class point str &optional (start 0) (end (length str)) (system:gc gcon))\"",
    ":draw-image-string",
    "\"(self class point str &optional (start 0) (end (length str)) (system:gc gcon))\"",
    ":draw-rectangle",
    "\"(self class point width height &optional (system:gc gcon))\"",
    ":draw-fill-rectangle",
    "\"(self class point width height &optional (system:gc gcon))\"",
    ":draw-arc",
    "\"(self class point width &optional (height width) (angle1 0.0) (angle2 2pi) (system:gc gcon))\"",
    ":draw-fill-arc",
    "\"(self class point width &optional (height width) (angle1 0.0) (angle2 2pi) (system:gc gcon))\"",
    ":drawline-primitive",
    "\"(self class x1 y1 x2 y2)\"",
    ":set-show-mode",
    "\"(self class)\"",
    ":set-erase-mode",
    "\"(self class)\"",
    ":set-xor-mode",
    "\"(self class)\"",
    "\"(self class &key (x 0) (y 0) (width (send self :width)) (height (send self :height)) ((:gc g) gcon))\"",
    "\"(self class)\"",
    ":graph",
    "\"(self class values &key (color) (max) (min) (system:gc gcon) (clear nil) (step))\"",
    ":3d-fill-rectangle",
    "\"(self class x y w h b lightedge darkedge surface topleft-edge &optional (state :flat))\"",
    "\"(self class &key (size 256) (width size) (height width) (depth (defaultdepth *display* 0)) (system:gc *defaultgc*) &allow-other-keys)\"",
    ":create-from-bitmap-file",
    "\"(self class fname)\"",
    "\"(self class fname)\"",
    "\"(self class)\"",
    "make-pixmaps",
    "\"(n &key (size 500) (width size) (height width) (system:gc *blackgc*))\"",
    "make-gray-pixmap",
    "\"(gray &key (foreground *fg-pixel*) (background *bg-pixel*) (depth (defaultdepth *display* 0)))\"",
    "make-gray-gc",
    "\"(gray &key (foreground *fg-pixel*) (background *bg-pixel*) (depth (defaultdepth *display* 0)))\"",
    "make-cleared-pixmap",
    "\"(width &optional (height width) (pixel *bg-pixel*))\"",
    "eventmask-to-value",
    "\"(events)\"",
    "gravity-to-value",
    "\"(g)\"",
    "\"(self class &key ((:parent par) *root*) (x 0) (y 0) (size 256) (width size) (height width) (border-width 2) (border *fg-pixel*) (save-under nil) (backing-store :always) ((:backing-pixmap backingpixmap) nil) (foreground) (background) (title (string (gensym \\\"WINDOW\\\"))) (event-mask 139279) ((:gc xgc)) (font) (name) (map t) ((:visual vi) *visual*) (depth (visual-depth vi)) (color-map) (override-redirect nil) (gravity :northwest) &allow-other-keys)\"",
    ":subwindows",
    "\"(self class &optional n)\"",
    "\"(self class)\"",
    "\"(self class)\"",
    ":remap",
    "\"(self class)\"",
    ":parent",
    "\"(self class)\"",
    "\"(self class child)\"",
    "\"(self class child)\"",
    ":reparent",
    "\"(self class par &optional (x 0) (y 0))\"",
    "\"(self class)\"",
    "\"(self class &aux attr)\"",
    ":event-mask",
    "\"(self class)\"",
    ":selectinput",
    "\"(self class event-mask)\"",
    "\"(self class)\"",
    ":location",
    "\"(self class &aux (attr (send self :attributes)))\"",
    "\"(self class &aux (attr (send self :attributes)))\"",
    "\"(self class)\"",
    ":screen",
    "\"(self class)\"",
    "\"(self class)\"",
    ":root",
    "\"(self class)\"",
    ":title",
    "\"(self class title)\"",
    "\"(self class &optional color)\"",
    ":background-pixmap",
    "\"(self class pixmap)\"",
    ":border",
    "\"(self class pixel)\"",
    ":save",
    "\"(self class)\"",
    ":refresh",
    "\"(self class)\"",
    ":move",
    "\"(self class newx newy)\"",
    ":resize",
    "\"(self class w h)\"",
    ":raise",
    "\"(self class)\"",
    ":lower",
    "\"(self class)\"",
    "\"(self class fname)\"",
    "\"(self class)\"",
    "\"(self class &key (x 0) (y 0) (width 0) (height 0))\"",
    ":set-colormap",
    "\"(self class cmap)\"",
    "\"(self class &rest args)\"",
    "geometry::default-viewsurface",
    "\"(&rest args)\"",
    "\"(self class points &optional (mode 0) (system:gc gcon))\"",
    ":draw-polygon",
    "\"(self class points &optional (system:gc gcon))\"",
    "\"(self class points &optional (shape 0) (coordmode 0) (system:gc gcon))\"",
    ":override_redirect",
    "\"(self class &optional (val 1))\"",
    ":save_under",
    "\"(self class &optional (val 1))\"",
    ":settransientforhint",
    "\"(self class)\"",
    "\"(self class)\"",
    ":global-pos",
    "\"(self class)\"",
    "make-xwindow",
    "\"(&rest args)\"",
    "find-xwindow",
    "\"(subname)\"",
    ":xeus",
    "\"@(#)$Id$\"",
    "provide",
  };
