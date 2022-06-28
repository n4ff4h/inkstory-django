module.exports = {
  content: [
    "../templates/**/*.html",
    "../../templates/**/*.html",
    "../../**/templates/**/*.html",
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        "dark-gray": "#292929",
      },
      fontFamily: {
        "rozha-one": ["Rozha One", "serif"],
        "roboto-mono": ["Roboto Mono", "sans-serif"],
      },
    },
    fontFamily: {
      poppins: ["Poppins", "sans-serif"],
    },
    container: {
      center: true,
      padding: "1rem",
    },
  },
  plugins: [require("@tailwindcss/typography"), require("flowbite/plugin")],
};
