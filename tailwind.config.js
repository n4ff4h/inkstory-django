module.exports = {
  content: [
    "./templates/**/*.html",
    "./**/templates/**/*.html",
    "./node_modules/flowbite/**/*.js",
    "./accounts/forms.py",
    "./posts/forms.py",
  ],
  theme: {
    container: {
      center: true,
      padding: "1rem",
    },
    colors: {
      brand: "#3B82F6",
      brand_darker: "#0B63F3",
      dark: "#0F172A",
      mid: "#CBD5E1",
      light: "#F8FAFC",
    },
  },
  plugins: [require("@tailwindcss/typography"), require("flowbite/plugin")],
};
