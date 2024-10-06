import React, { InputHTMLAttributes } from "react";

const Input = (props: InputHTMLAttributes<HTMLInputElement>) => {
  return (
    <input
      {...props}
      style={{
        height: "50px",
        border: "2px solid #000000",
        borderRadius: "20px",
        fontSize: "18px",
        width: "100%",
        padding: "5px 10px",
      }}
    />
  );
};

export { Input };
