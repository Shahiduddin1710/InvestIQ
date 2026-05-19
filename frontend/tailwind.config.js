/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        accent: {
          dark: '#c3ff00',
          light: '#198754',
        }
      }
    }
  },
  plugins: []
}
