#!/usr/bin/env python

import rospy
from jsk_rviz_plugins.msg import Pictogram
from random import random
rospy.init_node("pictogram_sample")
p = rospy.Publisher("/pictogram", Pictogram)

r = rospy.Rate(0.1)

pictograms = ["phone",
              "mobile",
              "mouse",
              "address",
              "mail",
              "paper-plane",
              "pencil",
              "feather",
              "attach",
              "inbox",
              "reply",
              "reply-all",
              "forward",
              "user",
              "users",
              "add-user",
              "vcard",
              "export",
              "location",
              "map",
              "compass",
              "direction",
              "hair-cross",
              "share",
              "shareable",
              "heart",
              "heart-empty",
              "star",
              "star-empty",
              "thumbs-up",
              "thumbs-down",
              "chat",
              "comment",
              "quote",
              "home",
              "popup",
              "search",
              "flashlight",
              "print",
              "bell",
              "link",
              "flag",
              "cog",
              "tools",
              "trophy",
              "tag",
              "camera",
              "megaphone",
              "moon",
              "palette",
              "leaf",
              "note",
              "beamed-note",
              "new",
              "graduation-cap",
              "book",
              "newspaper",
              "bag",
              "airplane",
              "lifebuoy",
              "eye",
              "clock",
              "mic",
              "calendar",
              "flash",
              "thunder-cloud",
              "droplet",
              "cd",
              "briefcase",
              "air",
              "hourglass",
              "gauge",
              "language",
              "network",
              "key",
              "battery",
              "bucket",
              "magnet",
              "drive",
              "cup",
              "rocket",
              "brush",
              "suitcase",
              "traffic-cone",
              "globe",
              "keyboard",
              "browser",
              "publish",
              "progress-3",
              "progress-2",
              "progress-1",
              "progress-0",
              "light-down",
              "light-up",
              "adjust",
              "code",
              "monitor",
              "infinity",
              "light-bulb",
              "credit-card",
              "database",
              "voicemail",
              "clipboard",
              "cart",
              "box",
              "ticket",
              "rss",
              "signal",
              "thermometer",
              "water",
              "sweden",
              "line-graph",
              "pie-chart",
              "bar-graph",
              "area-graph",
              "lock",
              "lock-open",
              "logout",
              "login",
              "check",
              "cross",
              "squared-minus",
              "squared-plus",
              "squared-cross",
              "circled-minus",
              "circled-plus",
              "circled-cross",
              "minus",
              "plus",
              "erase",
              "block",
              "info",
              "circled-info",
              "help",
              "circled-help",
              "warning",
              "cycle",
              "cw",
              "ccw",
              "shuffle",
              "back",
              "level-down",
              "retweet",
              "loop",
              "back-in-time",
              "level-up",
              "switch",
              "numbered-list",
              "add-to-list",
              "layout",
              "list",
              "text-doc",
              "text-doc-inverted",
              "doc",
              "docs",
              "landscape-doc",
              "picture",
              "video",
              "music",
              "folder",
              "archive",
              "trash",
              "upload",
              "download",
              "save",
              "install",
              "cloud",
              "upload-cloud",
              "bookmark",
              "bookmarks",
              "open-book",
              "play",
              "paus",
              "record",
              "stop",
              "ff",
              "fb",
              "to-start",
              "to-end",
              "resize-full",
              "resize-small",
              "volume",
              "sound",
              "mute",
              "flow-cascade",
              "flow-branch",
              "flow-tree",
              "flow-line",
              "flow-parallel",
              "left-bold",
              "down-bold",
              "up-bold",
              "right-bold",
              "left",
              "down",
              "up",
              "right",
              "circled-left",
              "circled-down",
              "circled-up",
              "circled-right",
              "triangle-left",
              "triangle-down",
              "triangle-up",
              "triangle-right",
              "chevron-left",
              "chevron-down",
              "chevron-up",
              "chevron-right",
              "chevron-small-left",
              "chevron-small-down",
              "chevron-small-up",
              "chevron-small-right",
              "chevron-thin-left",
              "chevron-thin-down",
              "chevron-thin-up",
              "chevron-thin-right",
              "left-thin",
              "down-thin",
              "up-thin",
              "right-thin",
              "arrow-combo",
              "three-dots",
              "two-dots",
              "dot",
              "cc",
              "cc-by",
              "cc-nc",
              "cc-nc-eu",
              "cc-nc-jp",
              "cc-sa",
              "cc-nd",
              "cc-pd",
              "cc-zero",
              "cc-share",
              "cc-remix",
              "db-logo",
              "db-shape",
              "github",
              "c-github",
              "flickr",
              "c-flickr",
              "vimeo",
              "c-vimeo",
              "twitter",
              "c-twitter",
              "facebook",
              "c-facebook",
              "s-facebook",
              "google+",
              "c-google+",
              "pinterest",
              "c-pinterest",
              "tumblr",
              "c-tumblr",
              "linkedin",
              "c-linkedin",
              "dribbble",
              "c-dribbble",
              "stumbleupon",
              "c-stumbleupon",
              "lastfm",
              "c-lastfm",
              "rdio",
              "c-rdio",
              "spotify",
              "c-spotify",
              "qq",
              "instagram",
              "dropbox",
              "evernote",
              "flattr",
              "skype",
              "c-skype",
              "renren",
              "sina-weibo",
              "paypal",
              "picasa",
              "soundcloud",
              "mixi",
              "behance",
              "google-circles",
              "vk",
              "smashing",
"fa-glass-martini",
"fa-music",
"fa-search",
"fa-heart",
"fa-star",
"fa-user",
"fa-film",
"fa-th-large",
"fa-th",
"fa-th-list",
"fa-check",
"fa-times",
"fa-search-plus",
"fa-search-minus",
"fa-power-off",
"fa-signal",
"fa-cog",
"fa-home",
"fa-clock",
"fa-road",
"fa-download",
"fa-inbox",
"fa-redo",
"fa-sync",
"fa-list-alt",
"fa-lock",
"fa-flag",
"fa-headphones",
"fa-volume-off",
"fa-volume-down",
"fa-volume-up",
"fa-qrcode",
"fa-barcode",
"fa-tag",
"fa-tags",
"fa-book",
"fa-bookmark",
"fa-print",
"fa-camera",
"fa-font",
"fa-bold",
"fa-italic",
"fa-text-height",
"fa-text-width",
"fa-align-left",
"fa-align-center",
"fa-align-right",
"fa-align-justify",
"fa-list",
"fa-outdent",
"fa-indent",
"fa-video",
"fa-image",
"fa-map-marker",
"fa-adjust",
"fa-tint",
"fa-edit",
"fa-step-backward",
"fa-fast-backward",
"fa-backward",
"fa-play",
"fa-pause",
"fa-stop",
"fa-forward",
"fa-fast-forward",
"fa-step-forward",
"fa-eject",
"fa-chevron-left",
"fa-chevron-right",
"fa-plus-circle",
"fa-minus-circle",
"fa-times-circle",
"fa-check-circle",
"fa-question-circle",
"fa-info-circle",
"fa-crosshairs",
"fa-ban",
"fa-arrow-left",
"fa-arrow-right",
"fa-arrow-up",
"fa-arrow-down",
"fa-share",
"fa-expand",
"fa-compress",
"fa-plus",
"fa-minus",
"fa-asterisk",
"fa-exclamation-circle",
"fa-gift",
"fa-leaf",
"fa-fire",
"fa-eye",
"fa-eye-slash",
"fa-exclamation-triangle",
"fa-plane",
"fa-calendar-alt",
"fa-random",
"fa-comment",
"fa-magnet",
"fa-chevron-up",
"fa-chevron-down",
"fa-retweet",
"fa-shopping-cart",
"fa-folder",
"fa-folder-open",
"fa-chart-bar",
"fa-twitter-square",
"fa-facebook-square",
"fa-camera-retro",
"fa-key",
"fa-cogs",
"fa-comments",
"fa-star-half",
"fa-linkedin",
"fa-thumbtack",
"fa-trophy",
"fa-github-square",
"fa-upload",
"fa-lemon",
"fa-phone",
"fa-phone-square",
"fa-twitter",
"fa-facebook",
"fa-github",
"fa-unlock",
"fa-credit-card",
"fa-rss",
"fa-hdd",
"fa-bullhorn",
"fa-certificate",
"fa-hand-point-right",
"fa-hand-point-left",
"fa-hand-point-up",
"fa-hand-point-down",
"fa-arrow-circle-left",
"fa-arrow-circle-right",
"fa-arrow-circle-up",
"fa-arrow-circle-down",
"fa-globe",
"fa-wrench",
"fa-tasks",
"fa-filter",
"fa-briefcase",
"fa-arrows-alt",
"fa-users",
"fa-link",
"fa-cloud",
"fa-flask",
"fa-cut",
"fa-copy",
"fa-paperclip",
"fa-save",
"fa-square",
"fa-bars",
"fa-list-ul",
"fa-list-ol",
"fa-strikethrough",
"fa-underline",
"fa-table",
"fa-magic",
"fa-truck",
"fa-pinterest",
"fa-pinterest-square",
"fa-google-plus-square",
"fa-google-plus-g",
"fa-money-bill",
"fa-caret-down",
"fa-caret-up",
"fa-caret-left",
"fa-caret-right",
"fa-columns",
"fa-sort",
"fa-sort-down",
"fa-sort-up",
"fa-envelope",
"fa-linkedin-in",
"fa-undo",
"fa-gavel",
"fa-bolt",
"fa-sitemap",
"fa-umbrella",
"fa-paste",
"fa-lightbulb",
"fa-user-md",
"fa-stethoscope",
"fa-suitcase",
"fa-bell",
"fa-coffee",
"fa-hospital",
"fa-ambulance",
"fa-medkit",
"fa-fighter-jet",
"fa-beer",
"fa-h-square",
"fa-plus-square",
"fa-angle-double-left",
"fa-angle-double-right",
"fa-angle-double-up",
"fa-angle-double-down",
"fa-angle-left",
"fa-angle-right",
"fa-angle-up",
"fa-angle-down",
"fa-desktop",
"fa-laptop",
"fa-tablet",
"fa-mobile",
"fa-quote-left",
"fa-quote-right",
"fa-spinner",
"fa-circle",
"fa-github-alt",
"fa-smile",
"fa-frown",
"fa-meh",
"fa-gamepad",
"fa-keyboard",
"fa-flag-checkered",
"fa-terminal",
"fa-code",
"fa-reply-all",
"fa-location-arrow",
"fa-crop",
"fa-code-branch",
"fa-unlink",
"fa-question",
"fa-info",
"fa-exclamation",
"fa-superscript",
"fa-subscript",
"fa-eraser",
"fa-puzzle-piece",
"fa-microphone",
"fa-microphone-slash",
"fa-calendar",
"fa-fire-extinguisher",
"fa-rocket",
"fa-maxcdn",
"fa-chevron-circle-left",
"fa-chevron-circle-right",
"fa-chevron-circle-up",
"fa-chevron-circle-down",
"fa-html5",
"fa-css3",
"fa-anchor",
"fa-unlock-alt",
"fa-bullseye",
"fa-ellipsis-h",
"fa-ellipsis-v",
"fa-rss-square",
"fa-play-circle",
"fa-minus-square",
"fa-check-square",
"fa-pen-square",
"fa-share-square",
"fa-compass",
"fa-caret-square-down",
"fa-caret-square-up",
"fa-caret-square-right",
"fa-euro-sign",
"fa-pound-sign",
"fa-dollar-sign",
"fa-rupee-sign",
"fa-yen-sign",
"fa-ruble-sign",
"fa-won-sign",
"fa-btc",
"fa-file",
"fa-file-alt",
"fa-sort-alpha-down",
"fa-sort-alpha-up",
"fa-sort-amount-down",
"fa-sort-amount-up",
"fa-sort-numeric-down",
"fa-sort-numeric-up",
"fa-thumbs-up",
"fa-thumbs-down",
"fa-youtube",
"fa-xing",
"fa-xing-square",
"fa-dropbox",
"fa-stack-overflow",
"fa-instagram",
"fa-flickr",
"fa-adn",
"fa-bitbucket",
"fa-tumblr",
"fa-tumblr-square",
"fa-apple",
"fa-windows",
"fa-android",
"fa-linux",
"fa-dribbble",
"fa-skype",
"fa-foursquare",
"fa-trello",
"fa-female",
"fa-male",
"fa-gratipay",
"fa-sun",
"fa-moon",
"fa-archive",
"fa-bug",
"fa-vk",
"fa-weibo",
"fa-renren",
"fa-pagelines",
"fa-stack-exchange",
"fa-caret-square-left",
"fa-dot-circle",
"fa-wheelchair",
"fa-vimeo-square",
"fa-lira-sign",
"fa-space-shuttle",
"fa-slack",
"fa-envelope-square",
"fa-wordpress",
"fa-openid",
"fa-university",
"fa-graduation-cap",
"fa-yahoo",
"fa-google",
"fa-reddit",
"fa-reddit-square",
"fa-stumbleupon-circle",
"fa-stumbleupon",
"fa-delicious",
"fa-digg",
"fa-pied-piper-pp",
"fa-pied-piper-alt",
"fa-drupal",
"fa-joomla",
"fa-language",
"fa-fax",
"fa-building",
"fa-child",
"fa-paw",
"fa-cube",
"fa-cubes",
"fa-behance",
"fa-behance-square",
"fa-steam",
"fa-steam-square",
"fa-recycle",
"fa-car",
"fa-taxi",
"fa-tree",
"fa-spotify",
"fa-deviantart",
"fa-soundcloud",
"fa-database",
"fa-file-pdf",
"fa-file-word",
"fa-file-excel",
"fa-file-powerpoint",
"fa-file-image",
"fa-file-archive",
"fa-file-audio",
"fa-file-video",
"fa-file-code",
"fa-vine",
"fa-codepen",
"fa-jsfiddle",
"fa-life-ring",
"fa-circle-notch",
"fa-rebel",
"fa-empire",
"fa-git-square",
"fa-git",
"fa-hacker-news",
"fa-tencent-weibo",
"fa-qq",
"fa-weixin",
"fa-paper-plane",
"fa-history",
"fa-heading",
"fa-paragraph",
"fa-sliders-h",
"fa-share-alt",
"fa-share-alt-square",
"fa-bomb",
"fa-futbol",
"fa-tty",
"fa-binoculars",
"fa-plug",
"fa-slideshare",
"fa-twitch",
"fa-yelp",
"fa-newspaper",
"fa-wifi",
"fa-calculator",
"fa-paypal",
"fa-google-wallet",
"fa-cc-visa",
"fa-cc-mastercard",
"fa-cc-discover",
"fa-cc-amex",
"fa-cc-paypal",
"fa-cc-stripe",
"fa-bell-slash",
"fa-trash",
"fa-copyright",
"fa-at",
"fa-eye-dropper",
"fa-paint-brush",
"fa-birthday-cake",
"fa-chart-area",
"fa-chart-pie",
"fa-chart-line",
"fa-lastfm",
"fa-lastfm-square",
"fa-toggle-off",
"fa-toggle-on",
"fa-bicycle",
"fa-bus",
"fa-ioxhost",
"fa-angellist",
"fa-closed-captioning",
"fa-shekel-sign",
"fa-buysellads",
"fa-connectdevelop",
"fa-dashcube",
"fa-forumbee",
"fa-leanpub",
"fa-sellsy",
"fa-shirtsinbulk",
"fa-simplybuilt",
"fa-skyatlas",
"fa-cart-plus",
"fa-cart-arrow-down",
"fa-ship",
"fa-user-secret",
"fa-motorcycle",
"fa-street-view",
"fa-heartbeat",
"fa-venus",
"fa-mars",
"fa-mercury",
"fa-transgender",
"fa-transgender-alt",
"fa-venus-double",
"fa-mars-double",
"fa-venus-mars",
"fa-mars-stroke",
"fa-mars-stroke-v",
"fa-mars-stroke-h",
"fa-neuter",
"fa-genderless",
"fa-pinterest-p",
"fa-whatsapp",
"fa-server",
"fa-user-plus",
"fa-user-times",
"fa-bed",
"fa-viacoin",
"fa-train",
"fa-subway",
"fa-medium",
"fa-y-combinator",
"fa-optin-monster",
"fa-opencart",
"fa-expeditedssl",
"fa-battery-full",
"fa-battery-three-quarters",
"fa-battery-half",
"fa-battery-quarter",
"fa-battery-empty",
"fa-mouse-pointer",
"fa-i-cursor",
"fa-object-group",
"fa-object-ungroup",
"fa-sticky-note",
"fa-cc-jcb",
"fa-cc-diners-club",
"fa-clone",
"fa-balance-scale",
"fa-hourglass-start",
"fa-hourglass-half",
"fa-hourglass-end",
"fa-hourglass",
"fa-hand-rock",
"fa-hand-paper",
"fa-hand-scissors",
"fa-hand-lizard",
"fa-hand-spock",
"fa-hand-pointer",
"fa-hand-peace",
"fa-trademark",
"fa-registered",
"fa-creative-commons",
"fa-gg",
"fa-gg-circle",
"fa-tripadvisor",
"fa-odnoklassniki",
"fa-odnoklassniki-square",
"fa-get-pocket",
"fa-wikipedia-w",
"fa-safari",
"fa-chrome",
"fa-firefox",
"fa-opera",
"fa-internet-explorer",
"fa-tv",
"fa-contao",
"fa-500px",
"fa-amazon",
"fa-calendar-plus",
"fa-calendar-minus",
"fa-calendar-times",
"fa-calendar-check",
"fa-industry",
"fa-map-pin",
"fa-map-signs",
"fa-map",
"fa-comment-alt",
"fa-houzz",
"fa-vimeo-v",
"fa-black-tie",
"fa-fonticons",
"fa-reddit-alien",
"fa-edge",
"fa-codiepie",
"fa-modx",
"fa-fort-awesome",
"fa-usb",
"fa-product-hunt",
"fa-mixcloud",
"fa-scribd",
"fa-pause-circle",
"fa-stop-circle",
"fa-shopping-bag",
"fa-shopping-basket",
"fa-hashtag",
"fa-bluetooth",
"fa-bluetooth-b",
"fa-percent",
"fa-gitlab",
"fa-wpbeginner",
"fa-wpforms",
"fa-envira",
"fa-universal-access",
"fa-blind",
"fa-audio-description",
"fa-phone-volume",
"fa-braille",
"fa-assistive-listening-systems",
"fa-american-sign-language-interpreting",
"fa-deaf",
"fa-glide",
"fa-glide-g",
"fa-sign-language",
"fa-low-vision",
"fa-viadeo",
"fa-viadeo-square",
"fa-snapchat",
"fa-snapchat-ghost",
"fa-snapchat-square",
"fa-pied-piper",
"fa-first-order",
"fa-yoast",
"fa-themeisle",
"fa-google-plus",
"fa-font-awesome",
"fa-handshake",
"fa-envelope-open",
"fa-linode",
"fa-address-book",
"fa-address-card",
"fa-user-circle",
"fa-id-badge",
"fa-id-card",
"fa-quora",
"fa-free-code-camp",
"fa-telegram",
"fa-thermometer-full",
"fa-thermometer-three-quarters",
"fa-thermometer-half",
"fa-thermometer-quarter",
"fa-thermometer-empty",
"fa-shower",
"fa-bath",
"fa-podcast",
"fa-window-maximize",
"fa-window-minimize",
"fa-window-restore",
"fa-bandcamp",
"fa-grav",
"fa-etsy",
"fa-imdb",
"fa-ravelry",
"fa-sellcast",
"fa-microchip",
"fa-snowflake",
"fa-superpowers",
"fa-wpexplorer",
"fa-meetup",
"fa-utensil-spoon",
"fa-utensils",
"fa-undo-alt",
"fa-trash-alt",
"fa-sync-alt",
"fa-stopwatch",
"fa-sign-out-alt",
"fa-sign-in-alt",
"fa-redo-alt",
"fa-poo",
"fa-images",
"fa-pencil-alt",
"fa-pen",
"fa-pen-alt",
"fa-long-arrow-alt-down",
"fa-long-arrow-alt-left",
"fa-long-arrow-alt-right",
"fa-long-arrow-alt-up",
"fa-expand-arrows-alt",
"fa-clipboard",
"fa-arrows-alt-h",
"fa-arrows-alt-v",
"fa-arrow-alt-circle-down",
"fa-arrow-alt-circle-left",
"fa-arrow-alt-circle-right",
"fa-arrow-alt-circle-up",
"fa-font-awesome-alt",
"fa-external-link-alt",
"fa-external-link-square-alt",
"fa-exchange-alt",
"fa-accessible-icon",
"fa-accusoft",
"fa-adversal",
"fa-affiliatetheme",
"fa-algolia",
"fa-amilia",
"fa-angrycreative",
"fa-app-store",
"fa-app-store-ios",
"fa-apper",
"fa-asymmetrik",
"fa-audible",
"fa-avianex",
"fa-aws",
"fa-bimobject",
"fa-bitcoin",
"fa-bity",
"fa-blackberry",
"fa-blogger",
"fa-blogger-b",
"fa-buromobelexperte",
"fa-centercode",
"fa-cloud-download-alt",
"fa-cloud-upload-alt",
"fa-cloudscale",
"fa-cloudsmith",
"fa-cloudversify",
"fa-cpanel",
"fa-css3-alt",
"fa-cuttlefish",
"fa-d-and-d",
"fa-deploydog",
"fa-deskpro",
"fa-digital-ocean",
"fa-discord",
"fa-discourse",
"fa-dochub",
"fa-docker",
"fa-draft2digital",
"fa-dribbble-square",
"fa-dyalog",
"fa-earlybirds",
"fa-erlang",
"fa-facebook-f",
"fa-facebook-messenger",
"fa-firstdraft",
"fa-fonticons-fi",
"fa-fort-awesome-alt",
"fa-freebsd",
"fa-gem",
"fa-gitkraken",
"fa-gofore",
"fa-goodreads",
"fa-goodreads-g",
"fa-google-drive",
"fa-google-play",
"fa-gripfire",
"fa-grunt",
"fa-gulp",
"fa-hacker-news-square",
"fa-hire-a-helper",
"fa-hotjar",
"fa-hubspot",
"fa-itunes",
"fa-itunes-note",
"fa-jenkins",
"fa-joget",
"fa-js",
"fa-js-square",
"fa-keycdn",
"fa-kickstarter",
"fa-kickstarter-k",
"fa-laravel",
"fa-level-down-alt",
"fa-level-up-alt",
"fa-line",
"fa-lock-open",
"fa-lyft",
"fa-magento",
"fa-map-marker-alt",
"fa-medapps",
"fa-medium-m",
"fa-medrt",
"fa-microphone-alt",
"fa-microsoft",
"fa-mix",
"fa-mizuni",
"fa-mobile-alt",
"fa-monero",
"fa-money-bill-alt",
"fa-napster",
"fa-node-js",
"fa-npm",
"fa-ns8",
"fa-nutritionix",
"fa-page4",
"fa-palfed",
"fa-patreon",
"fa-periscope",
"fa-phabricator",
"fa-phoenix-framework",
"fa-phone-slash",
"fa-playstation",
"fa-portrait",
"fa-pushed",
"fa-python",
"fa-red-river",
"fa-wpressr",
"fa-reply",
"fa-replyd",
"fa-resolving",
"fa-rocketchat",
"fa-rockrms",
"fa-schlix",
"fa-searchengin",
"fa-servicestack",
"fa-shield-alt",
"fa-sistrix",
"fa-slack-hash",
"fa-speakap",
"fa-staylinked",
"fa-steam-symbol",
"fa-sticker-mule",
"fa-studiovinari",
"fa-supple",
"fa-tablet-alt",
"fa-tachometer-alt",
"fa-telegram-plane",
"fa-ticket-alt",
"fa-uber",
"fa-uikit",
"fa-uniregistry",
"fa-untappd",
"fa-user-alt",
"fa-ussunnah",
"fa-vaadin",
"fa-viber",
"fa-vimeo",
"fa-vnv",
"fa-whatsapp-square",
"fa-whmcs",
"fa-window-close",
"fa-wordpress-simple",
"fa-xbox",
"fa-yandex",
"fa-yandex-international",
"fa-apple-pay",
"fa-cc-apple-pay",
"fa-fly",
"fa-node",
"fa-osi",
"fa-react",
"fa-autoprefixer",
"fa-less",
"fa-sass",
"fa-vuejs",
"fa-angular",
"fa-aviato",
"fa-compress-alt",
"fa-ember",
"fa-expand-alt",
"fa-font-awesome-flag",
"fa-gitter",
"fa-hooli",
"fa-strava",
"fa-stripe",
"fa-stripe-s",
"fa-typo3",
"fa-amazon-pay",
"fa-cc-amazon-pay",
"fa-ethereum",
"fa-korvue",
"fa-elementor",
"fa-youtube-square",
"fa-baseball-ball",
"fa-basketball-ball",
"fa-bowling-ball",
"fa-chess",
"fa-chess-bishop",
"fa-chess-board",
"fa-chess-king",
"fa-chess-knight",
"fa-chess-pawn",
"fa-chess-queen",
"fa-chess-rook",
"fa-dumbbell",
"fa-flipboard",
"fa-football-ball",
"fa-golf-ball",
"fa-hips",
"fa-hockey-puck",
"fa-php",
"fa-quidditch",
"fa-quinscape",
"fa-square-full",
"fa-table-tennis",
"fa-volleyball-ball",
"fa-allergies",
"fa-band-aid",
"fa-box",
"fa-boxes",
"fa-briefcase-medical",
"fa-burn",
"fa-capsules",
"fa-clipboard-check",
"fa-clipboard-list",
"fa-diagnoses",
"fa-dna",
"fa-dolly",
"fa-dolly-flatbed",
"fa-file-medical",
"fa-file-medical-alt",
"fa-first-aid",
"fa-hospital-alt",
"fa-hospital-symbol",
"fa-id-card-alt",
"fa-notes-medical",
"fa-pallet",
"fa-pills",
"fa-prescription-bottle",
"fa-prescription-bottle-alt",
"fa-procedures",
"fa-shipping-fast",
"fa-smoking",
"fa-syringe",
"fa-tablets",
"fa-thermometer",
"fa-vial",
"fa-vials",
"fa-warehouse",
"fa-weight",
"fa-x-ray",
"fa-box-open",
"fa-comment-dots",
"fa-comment-slash",
"fa-couch",
"fa-donate",
"fa-dove",
"fa-hand-holding",
"fa-hand-holding-heart",
"fa-hand-holding-usd",
"fa-hands",
"fa-hands-helping",
"fa-parachute-box",
"fa-people-carry",
"fa-piggy-bank",
"fa-readme",
"fa-ribbon",
"fa-route",
"fa-seedling",
"fa-sign",
"fa-smile-wink",
"fa-tape",
"fa-truck-loading",
"fa-truck-moving",
"fa-video-slash",
"fa-wine-glass",
"fa-java",
"fa-pied-piper-hat",
"fa-font-awesome-logo-full",
"fa-creative-commons-by",
"fa-creative-commons-nc",
"fa-creative-commons-nc-eu",
"fa-creative-commons-nc-jp",
"fa-creative-commons-nd",
"fa-creative-commons-pd",
"fa-creative-commons-pd-alt",
"fa-creative-commons-remix",
"fa-creative-commons-sa",
"fa-creative-commons-sampling",
"fa-creative-commons-sampling-plus",
"fa-creative-commons-share",
"fa-creative-commons-zero",
"fa-ebay",
"fa-keybase",
"fa-mastodon",
"fa-r-project",
"fa-researchgate",
"fa-teamspeak",
"fa-user-alt-slash",
"fa-user-astronaut",
"fa-user-check",
"fa-user-clock",
"fa-user-cog",
"fa-user-edit",
"fa-user-friends",
"fa-user-graduate",
"fa-user-lock",
"fa-user-minus",
"fa-user-ninja",
"fa-user-shield",
"fa-user-slash",
"fa-user-tag",
"fa-user-tie",
"fa-users-cog",
"fa-first-order-alt",
"fa-fulcrum",
"fa-galactic-republic",
"fa-galactic-senate",
"fa-jedi-order",
"fa-mandalorian",
"fa-old-republic",
"fa-phoenix-squadron",
"fa-sith",
"fa-trade-federation",
"fa-wolf-pack-battalion",
"fa-balance-scale-left",
"fa-balance-scale-right",
"fa-blender",
"fa-book-open",
"fa-broadcast-tower",
"fa-broom",
"fa-chalkboard",
"fa-chalkboard-teacher",
"fa-church",
"fa-coins",
"fa-compact-disc",
"fa-crow",
"fa-crown",
"fa-dice",
"fa-dice-five",
"fa-dice-four",
"fa-dice-one",
"fa-dice-six",
"fa-dice-three",
"fa-dice-two",
"fa-divide",
"fa-door-closed",
"fa-door-open",
"fa-equals",
"fa-feather",
"fa-frog",
"fa-gas-pump",
"fa-glasses",
"fa-greater-than",
"fa-greater-than-equal",
"fa-helicopter",
"fa-infinity",
"fa-kiwi-bird",
"fa-less-than",
"fa-less-than-equal",
"fa-memory",
"fa-microphone-alt-slash",
"fa-money-bill-wave",
"fa-money-bill-wave-alt",
"fa-money-check",
"fa-money-check-alt",
"fa-not-equal",
"fa-palette",
"fa-parking",
"fa-percentage",
"fa-project-diagram",
"fa-receipt",
"fa-robot",
"fa-ruler",
"fa-ruler-combined",
"fa-ruler-horizontal",
"fa-ruler-vertical",
"fa-school",
"fa-screwdriver",
"fa-shoe-prints",
"fa-skull",
"fa-smoking-ban",
"fa-store",
"fa-store-alt",
"fa-stream",
"fa-stroopwafel",
"fa-toolbox",
"fa-tshirt",
"fa-walking",
"fa-wallet",
"fa-angry",
"fa-archway",
"fa-atlas",
"fa-award",
"fa-backspace",
"fa-bezier-curve",
"fa-bong",
"fa-brush",
"fa-bus-alt",
"fa-cannabis",
"fa-check-double",
"fa-cocktail",
"fa-concierge-bell",
"fa-cookie",
"fa-cookie-bite",
"fa-crop-alt",
"fa-digital-tachograph",
"fa-dizzy",
"fa-drafting-compass",
"fa-drum",
"fa-drum-steelpan",
"fa-feather-alt",
"fa-file-contract",
"fa-file-download",
"fa-file-export",
"fa-file-import",
"fa-file-invoice",
"fa-file-invoice-dollar",
"fa-file-prescription",
"fa-file-signature",
"fa-file-upload",
"fa-fill",
"fa-fill-drip",
"fa-fingerprint",
"fa-fish",
"fa-flushed",
"fa-frown-open",
"fa-glass-martini-alt",
"fa-globe-africa",
"fa-globe-americas",
"fa-globe-asia",
"fa-grimace",
"fa-grin",
"fa-grin-alt",
"fa-grin-beam",
"fa-grin-beam-sweat",
"fa-grin-hearts",
"fa-grin-squint",
"fa-grin-squint-tears",
"fa-grin-stars",
"fa-grin-tears",
"fa-grin-tongue",
"fa-grin-tongue-squint",
"fa-grin-tongue-wink",
"fa-grin-wink",
"fa-grip-horizontal",
"fa-grip-vertical",
"fa-headphones-alt",
"fa-headset",
"fa-highlighter",
"fa-hornbill",
"fa-hot-tub",
"fa-hotel",
"fa-joint",
"fa-kiss",
"fa-kiss-beam",
"fa-kiss-wink-heart",
"fa-laugh",
"fa-laugh-beam",
"fa-laugh-squint",
"fa-laugh-wink",
"fa-luggage-cart",
"fa-mailchimp",
"fa-map-marked",
"fa-map-marked-alt",
"fa-marker",
"fa-medal",
"fa-megaport",
"fa-meh-blank",
"fa-meh-rolling-eyes",
"fa-monument",
"fa-mortar-pestle",
"fa-nimblr",
"fa-paint-roller",
"fa-passport",
"fa-pen-fancy",
"fa-pen-nib",
"fa-pencil-ruler",
"fa-plane-arrival",
"fa-plane-departure",
"fa-prescription",
"fa-rev",
"fa-sad-cry",
"fa-sad-tear",
"fa-shopware",
"fa-shuttle-van",
"fa-signature",
"fa-smile-beam",
"fa-solar-panel",
"fa-spa",
"fa-splotch",
"fa-spray-can",
"fa-squarespace",
"fa-stamp",
"fa-star-half-alt",
"fa-suitcase-rolling",
"fa-surprise",
"fa-swatchbook",
"fa-swimmer",
"fa-swimming-pool",
"fa-themeco",
"fa-tint-slash",
"fa-tired",
"fa-tooth",
"fa-umbrella-beach",
"fa-vector-square",
"fa-weebly",
"fa-weight-hanging",
"fa-wine-glass-alt",
"fa-wix",
"fa-air-freshener",
"fa-apple-alt",
"fa-atom",
"fa-bone",
"fa-book-reader",
"fa-brain",
"fa-car-alt",
"fa-car-battery",
"fa-car-crash",
"fa-car-side",
"fa-charging-station",
"fa-directions",
"fa-draw-polygon",
"fa-ello",
"fa-hackerrank",
"fa-kaggle",
"fa-laptop-code",
"fa-layer-group",
"fa-markdown",
"fa-microscope",
"fa-neos",
"fa-oil-can",
"fa-poop",
"fa-shapes",
"fa-star-of-life",
"fa-teeth",
"fa-teeth-open",
"fa-theater-masks",
"fa-traffic-light",
"fa-truck-monster",
"fa-truck-pickup",
"fa-zhihu",
"fa-ad",
"fa-alipay",
"fa-ankh",
"fa-bible",
"fa-business-time",
"fa-city",
"fa-comment-dollar",
"fa-comments-dollar",
"fa-cross",
"fa-dharmachakra",
"fa-envelope-open-text",
"fa-folder-minus",
"fa-folder-plus",
"fa-funnel-dollar",
"fa-gopuram",
"fa-hamsa",
"fa-bahai",
"fa-jedi",
"fa-journal-whills",
"fa-kaaba",
"fa-khanda",
"fa-landmark",
"fa-mail-bulk",
"fa-menorah",
"fa-mosque",
"fa-om",
"fa-pastafarianism",
"fa-peace",
"fa-place-of-worship",
"fa-poll",
"fa-poll-h",
"fa-pray",
"fa-praying-hands",
"fa-quran",
"fa-search-dollar",
"fa-search-location",
"fa-socks",
"fa-square-root-alt",
"fa-star-and-crescent",
"fa-star-of-david",
"fa-synagogue",
"fa-the-red-yeti",
"fa-torah",
"fa-torii-gate",
"fa-vihara",
"fa-volume-mute",
"fa-yin-yang",
"fa-acquisitions-incorporated",
"fa-blender-phone",
"fa-book-dead",
"fa-campground",
"fa-cat",
"fa-chair",
"fa-cloud-moon",
"fa-cloud-sun",
"fa-critical-role",
"fa-d-and-d-beyond",
"fa-dev",
"fa-dice-d20",
"fa-dice-d6",
"fa-dog",
"fa-dragon",
"fa-drumstick-bite",
"fa-dungeon",
"fa-fantasy-flight-games",
"fa-file-csv",
"fa-fist-raised",
"fa-ghost",
"fa-hammer",
"fa-hanukiah",
"fa-hat-wizard",
"fa-hiking",
"fa-hippo",
"fa-horse",
"fa-house-damage",
"fa-hryvnia",
"fa-mask",
"fa-mountain",
"fa-network-wired",
"fa-otter",
"fa-penny-arcade",
"fa-ring",
"fa-running",
"fa-scroll",
"fa-skull-crossbones",
"fa-slash",
"fa-spider",
"fa-toilet-paper",
"fa-tractor",
"fa-user-injured",
"fa-vr-cardboard",
"fa-wind",
"fa-wine-bottle",
"fa-wizards-of-the-coast",
"fa-think-peaks",
"fa-cloud-meatball",
"fa-cloud-moon-rain",
"fa-cloud-rain",
"fa-cloud-showers-heavy",
"fa-cloud-sun-rain",
"fa-democrat",
"fa-flag-usa",
"fa-meteor",
"fa-person-booth",
"fa-poo-storm",
"fa-rainbow",
"fa-reacteurope",
"fa-republican",
"fa-smog",
"fa-temperature-high",
"fa-temperature-low",
"fa-vote-yea",
"fa-water",
"fa-adobe",
"fa-artstation",
"fa-atlassian",
"fa-baby",
"fa-baby-carriage",
"fa-biohazard",
"fa-blog",
"fa-calendar-day",
"fa-calendar-week",
"fa-canadian-maple-leaf",
"fa-candy-cane",
"fa-carrot",
"fa-cash-register",
"fa-centos",
"fa-compress-arrows-alt",
"fa-confluence",
"fa-dhl",
"fa-diaspora",
"fa-dumpster",
"fa-dumpster-fire",
"fa-ethernet",
"fa-fedex",
"fa-fedora",
"fa-figma",
"fa-gifts",
"fa-glass-cheers",
"fa-glass-whiskey",
"fa-globe-europe",
"fa-grip-lines",
"fa-grip-lines-vertical",
"fa-guitar",
"fa-heart-broken",
"fa-holly-berry",
"fa-horse-head",
"fa-icicles",
"fa-igloo",
"fa-intercom",
"fa-invision",
"fa-jira",
"fa-mendeley",
"fa-mitten",
"fa-mug-hot",
"fa-radiation",
"fa-radiation-alt",
"fa-raspberry-pi",
"fa-redhat",
"fa-restroom",
"fa-satellite",
"fa-satellite-dish",
"fa-sd-card",
"fa-sim-card",
"fa-skating",
"fa-sketch",
"fa-skiing",
"fa-skiing-nordic",
"fa-sleigh",
"fa-sms",
"fa-snowboarding",
"fa-snowman",
"fa-snowplow",
"fa-sourcetree",
"fa-suse",
"fa-tenge",
"fa-toilet",
"fa-tools",
"fa-tram",
"fa-ubuntu",
"fa-ups",
"fa-usps",
"fa-yarn",
"fa-fire-alt",
"fa-bacon",
"fa-book-medical",
"fa-bread-slice",
"fa-cheese",
"fa-clinic-medical",
"fa-comment-medical",
"fa-crutch",
"fa-egg",
"fa-hamburger",
"fa-hand-middle-finger",
"fa-hard-hat",
"fa-hotdog",
"fa-ice-cream",
"fa-laptop-medical",
"fa-pager",
"fa-pepper-hot",
"fa-pizza-slice",
"fa-trash-restore",
"fa-trash-restore-alt",
"fa-user-nurse",
"fa-airbnb",
"fa-battle-net",
"fa-bootstrap",
"fa-buffer",
"fa-chromecast",
"fa-evernote",
"fa-itch-io",
"fa-salesforce",
"fa-speaker-deck",
"fa-symfony",
"fa-wave-square",
"fa-waze",
"fa-yammer",
"fa-git-alt",
"fa-stackpath",
"fa-biking",
"fa-border-all",
"fa-border-none",
"fa-border-style",
"fa-fan",
"fa-icons",
"fa-phone-alt",
"fa-phone-square-alt",
"fa-photo-video",
"fa-remove-format",
"fa-sort-alpha-down-alt",
"fa-sort-alpha-up-alt",
"fa-sort-amount-down-alt",
"fa-sort-amount-up-alt",
"fa-sort-numeric-down-alt",
"fa-sort-numeric-up-alt",
"fa-spell-check",
"fa-voicemail",
"fa-cotton-bureau",
"fa-buy-n-large",
"fa-hat-cowboy",
"fa-hat-cowboy-side",
"fa-mdb",
"fa-mouse",
"fa-orcid",
"fa-record-vinyl",
"fa-swift",
"fa-umbraco",
"fa-caravan",
"fa-firefox-browser",
"fa-ideal",
"fa-microblog",
"fa-pied-piper-square",
"fa-trailer",
"fa-unity"]

counter = 0
while not rospy.is_shutdown():
    msg = Pictogram()
    msg.action = Pictogram.JUMP_ONCE
    msg.header.frame_id = "base_link"
    msg.header.stamp = rospy.Time.now()
    msg.pose.position.z = 1.6
    msg.pose.orientation.w = 0.7
    msg.pose.orientation.x = 0
    msg.pose.orientation.y = -0.7
    msg.pose.orientation.z = 0
    msg.mode = Pictogram.PICTOGRAM_MODE
    msg.speed = 1.0
    # msg.ttl = 5.0
    msg.size = 1
    msg.color.r = 25 / 255.0
    msg.color.g = 255 / 255.0
    msg.color.b = 240 / 255.0
    msg.color.a = 1.0
    msg.character = pictograms[counter]
    p.publish(msg)
    r.sleep()
    counter = counter + 1
    if len(pictograms) == counter:
        counter = 0
