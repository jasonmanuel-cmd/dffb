/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{astro,html,js,jsx,md}"],
  theme: {
    extend: {
      colors: {
        navy: "#0c1f45",
        "navy-dark": "#08142f",
        beige: "#f3e8d5",
        gold: "#c8a354",
        "text-light": "#dbe3f5",
        "text-dark": "#1b2337",
        alert: "#d93025",
      },
      fontFamily: {
        sans: ["Inter", "system-ui", "sans-serif"],
      },
    },
  },
  plugins: [],
};
