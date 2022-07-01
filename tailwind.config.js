module.exports = {
  content: [
    "./templates/**/*.html",
    "./**/templates/**/*.html",
    "./node_modules/flowbite/**/*.js",
    "./accounts/forms.py",
  ],
  theme: {
    container: {
      center: true,
      padding: "1rem",
    },
  },
  plugins: [require("@tailwindcss/typography"), require("flowbite/plugin")],
};
