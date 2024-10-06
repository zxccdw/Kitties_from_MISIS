import React from "react";
import { UniversalButton } from "@components/Buttons/UniversalButton";
import Image from "next/image";
import GoogleLogo from "@assets/svg/google.svg";
import TelegramLogo from "@assets/svg/telegram.svg";
import VKLogo from "@assets/svg/vk.svg";
import styles from "./SocialLoginButtonBlock.module.scss";

type Props = {};

const SocialLoginButtonBlock = (props: Props) => {
  const logoWidth = 30;
  return (
    <div className={styles.slbb}>
      <UniversalButton color="red" backColor="transparent" border>
        Войти с помощью
        <Image src={GoogleLogo} alt="Google logo" width={logoWidth} />
      </UniversalButton>
      <UniversalButton color="red" backColor="transparent" border>
        Войти с помощью
        <Image src={TelegramLogo} alt="Telegram logo" width={logoWidth} />
      </UniversalButton>
      <UniversalButton color="red" backColor="transparent" border>
        Войти с помощью
        <Image src={VKLogo} alt="VK logo" width={logoWidth} />
      </UniversalButton>
    </div>
  );
};

export { SocialLoginButtonBlock };
