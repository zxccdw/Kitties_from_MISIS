import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";
import { NavigationBar } from "./src/components/NavigationBar/NavigationBar";

const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

export const metadata: Metadata = {
  title: "ФК Кокос",
  description: "Страница футбольного клуба Кокос Групп",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ru">
      <body className={`${geistSans.variable} ${geistMono.variable}`}>
        <NavigationBar />
        {children}
      </body>
    </html>
  );
}
