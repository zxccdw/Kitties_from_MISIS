"use client";

import React from "react";
import styles from "./LoginForm.module.scss";
import { Input } from "@components/Input/Input";
import { UniversalButton } from "@components/Buttons/UniversalButton";
type Props = {};

const LoginForm = (props: Props) => {
  const onSubmit = () => {
    return;
  };
  return (
    <div className={styles.lf}>
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
