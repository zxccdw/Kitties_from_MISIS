"use client";

import React from "react";
import styles from "./LoginForm.module.scss";
import { SocialLoginButtonBlock } from "@components/SocialLoginButtonBlock/SocialLoginButtonBlock";
import { Input } from "@components/Input/Input";
type Props = {};

const LoginForm = (props: Props) => {
  return (
    <div className={styles.lf}>
      <SocialLoginButtonBlock />
      <form action="">
        <Input placeholder="Email" type="email" />
        <Input placeholder="Пароль" type="password" />
      </form>
    </div>
  );
};

export { LoginForm };
