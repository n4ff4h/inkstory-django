module.exports = {
    content: [
        "./templates/**/*.html",
        "./posts/templates/**/*.html",
        "./accounts/templates/**/*.html",
        "./node_modules/flowbite/**/*.js",
    ],
    theme: {
        extend: {
            colors: {
                'dark-gray': '#292929',
            },
            fontFamily: {
                'noto-sans': ['Noto Sans', 'sans-serif'],
                'rozha-one': ['Rozha One', 'serif'],
                'roboto-mono': ['Roboto Mono', 'sans-serif'],
            },
        },
        fontFamily: {
            'poppins': ['Poppins', 'sans-serif'],
        },
        container: {
            center: true,
            padding: '1rem',
            screens: {
                sm: '640px',
                md: '768px',
                lg: '1024px',
                xl: '1280px',
                '2xl': '1536px',
            },
        },
    },
    plugins: [require("flowbite/plugin")],
};
