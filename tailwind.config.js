module.exports = {
  content: [
    "./templates/**/*.html",
    "./posts/templates/**/*.html",
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("flowbite/plugin")],
};
