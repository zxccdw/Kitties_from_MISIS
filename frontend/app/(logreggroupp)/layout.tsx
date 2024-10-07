import type { Metadata } from "next";
import Image from "next/image";
import KokosGrLogo from "@assets/logos/kokos_group_logo.png";
import styles from "./layout.module.scss";
import { SocialLoginButtonBlock } from "../src/components/SocialLoginButtonBlock/SocialLoginButtonBlock";

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
      <div className={styles.welcText}>
        <div className={styles.welcText__title}>
          <p className={styles.welcText__titleText}>Добро пожаловать!</p>
        </div>
        <div className={styles.welcText__main}>
          <p className={styles.welcText__mainText}>
            Присоединяйся сейчас, смотри матчи в прямом эфире и обсуждай их с
            фанатами.
          </p>
        </div>
      </div>
      <SocialLoginButtonBlock />
      {children}
    </div>
  );
}
