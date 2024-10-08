import type { Metadata } from "next";
import Image from "next/image";
import KokosGrLogo from "@assets/logos/kokos_group_logo.png";
import styles from "./layout.module.scss";

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
    <div className={styles.ll}>
      <Image src={KokosGrLogo} alt="Kokos group logo" />
      <div className={styles.ll__greetings}>
        <h1>Добро пожаловать!</h1>
        <p>
          Присоединяйся сейчас,
          <br />
          смотри матчи в прямом эфире
          <br />и обсуждай их с фанатами
        </p>
      </div>
      {children}
    </div>
  );
}
