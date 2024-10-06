import Large_logo from "@assets/logos/kokos_logo_large.png";
import Image from "next/image";
import styles from "./page.module.scss";
import { UniversalButton } from "@components/Buttons/UniversalButton";

export default function Home() {
  return (
    <div className={styles.mp}>
      <Image src={Large_logo} alt="Kokos_logo" />
      <div className={styles.mp__greetings}>
        <h1>Добро пожаловать!</h1>
        <p>
          Присоединяйся сейчас,
          <br />
          смотри матчи в прямом эфире
          <br />и обсуждай их с фанатами
        </p>
      </div>
      <UniversalButton color="white" backColor="red" border={false}>
        Зарегистрироваться
      </UniversalButton>
      <UniversalButton color="black" backColor="transparent" border={false}>
        Уже есть аккаунт
      </UniversalButton>
    </div>
  );
}
