import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './src/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        compass: {
          navy: '#0F172A',
          gold: '#F59E0B',
          emerald: '#10B981',
          rose: '#F43F5E',
          slate: '#64748B',
        },
      },
    },
  },
  plugins: [],
}
export default config