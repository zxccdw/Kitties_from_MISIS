"use client";

import React from "react";
import styles from "./LoginForm.module.scss";
import { SocialLoginButtonBlock } from "@components/SocialLoginButtonBlock/SocialLoginButtonBlock";
import { Input } from "@components/Input/Input";
type Props = {};

const LoginForm = (props: Props) => {
  return (
    <div className={styles.lf}>
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
      <form
        action=""
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
          width: "450px",
        }}
      >
        <Input placeholder="Email" type="email" />
        <Input placeholder="Пароль" type="password" />
        <input
          type="submit"
          value={"Войти"}
          style={{
            fontSize: "18px",
            padding: "5px 15px",
            marginTop: "20px",
            borderRadius: "10px",
            border: "2px solid red",
            color: "red",
            backgroundColor: "white",
            cursor: "pointer",
          }}
        />
      </form>
    </div>
  );
};

export { LoginForm };
