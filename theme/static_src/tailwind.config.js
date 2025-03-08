module.exports = {
  content: [
    "../templates/**/*.html",
    "../../templates/**/*.html",
    "../../**/templates/**/*.html",
  ],
  theme: {
    extend: {
      fontFamily: {},
      colors: {
        theme_color2: {
          400: "rgb(115 130 82 / var(--tw-text-opacity,1))",
          300: "rgb(167 200 121 / var(--tw-bg-opacity, 1))",
          200: "rgb(205 234 152 / var(--tw-bg-opacity, 1))",
          100: "rgb(224 244 179 / var(--tw-bg-opacity,1))",
        },
        bg_theme_color1: {
          600: "rgb(35 35 35 / var(--tw-bg-opacity, 1))",
        },
      },
    },
  },
  plugins: [
    require("@tailwindcss/forms"),
    require("@tailwindcss/typography"),
    require("@tailwindcss/aspect-ratio"),
  ],
};
