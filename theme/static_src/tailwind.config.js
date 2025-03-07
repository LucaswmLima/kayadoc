/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
  content: [
    "../templates/**/*.html",

    "../../templates/**/*.html",

    "../../**/templates/**/*.html",
  ],
  theme: {
    extend: {
        fontFamily: {
            custom: ['Roboto', 'sans-serif'],
          },
      colors: {
        theme_color2: {
          400: "rgb(115 130 82)",
          300: "rgb(205 234 152)",
        },
      },
    },
  },
  plugins: [
    /**
     * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
     * for forms. If you don't like it or have own styling for forms,
     * comment the line below to disable '@tailwindcss/forms'.
     */
    require("@tailwindcss/forms"),
    require("@tailwindcss/typography"),
    require("@tailwindcss/aspect-ratio"),
  ],
};
