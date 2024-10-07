import type { Metadata } from "next";
import Image from "next/image";
import KokosGrLogo from "@assets/logos/kokos_group_logo.png";
import localFont from "next/font/local";
import { NavigationBar } from "@components/NavigationBar/NavigationBar";

export const metadata: Metadata = {
  title: "ФК Кокос",
  description: "Страница футбольного клуба Кокос Групп",
};

export default function LoginLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      {/* <NavigationBar /> */}
      <Image src={KokosGrLogo} alt="Kokos group logo" />
      {children}
    </div>
  );
}
