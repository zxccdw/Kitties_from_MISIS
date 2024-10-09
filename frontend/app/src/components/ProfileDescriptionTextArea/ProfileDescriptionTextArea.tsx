"use client";

import React, { useState } from "react";

type Props = {};

const ProfileDescriptionTextArea = (props: Props) => {
  const [text, setText] = useState<string>("");
  return (
    <textarea
      name="description"
      id="description"
      value={text}
      onChange={(e) => setText(e.target.value)}
      style={{
        minBlockSize: "200px",
        minWidth: "700px",
        border: "2px solid #D9D9D9",
        borderRadius: "20px",
        resize: "none",
      }}
    ></textarea>
  );
};

export { ProfileDescriptionTextArea };
