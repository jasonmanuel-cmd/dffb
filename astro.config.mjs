import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";
import netlify from "@astrojs/netlify";

export default defineConfig({
  output: "static",
  site: "https://dffbseniorliving.com",
  adapter: netlify(),
  integrations: [tailwind()],
});
