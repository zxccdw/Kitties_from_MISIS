"use client";

import React from "react";
import styles from "./LoginForm.module.scss";
import { SocialLoginButtonBlock } from "@components/SocialLoginButtonBlock/SocialLoginButtonBlock";
import { Input } from "@components/Input/Input";
import { UniversalButton } from "@components/Buttons/UniversalButton";
type Props = {};

const LoginForm = (props: Props) => {
  const onSubmit = () => {
    return;
  };
  return (
    <div className={styles.lf}>
      <SocialLoginButtonBlock />
      <form action="" className={styles.lf__form}>
        <div className={styles.lf__form__field}>
          <label htmlFor="email">Электронная почта</label>
          <Input placeholder="Email" type="email" id="email" />
        </div>
        <div className={styles.lf__form__field}>
          <label htmlFor="password">Пароль</label>
          <Input placeholder="Пароль" type="password" id="password" />
        </div>
        <UniversalButton
          onClick={onSubmit}
          color="red"
          backColor="transparent"
          border
        >
          Войти
        </UniversalButton>
      </form>
    </div>
  );
};

export { LoginForm };
