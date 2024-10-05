"use client";

import React from "react";
import styled, { css } from "styled-components";

type Props = {
  color: "red" | "white" | "black";
  backColor: "transparent" | "red";
  border: boolean;
  children: React.ReactNode;
};

const StyledButton = styled.button<Props>`
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
  color: ${({ color = "white" }) => {
    switch (color) {
      case "black":
        return "#000000";
      case "red":
        return "#E13B39";
      case "white":
        return "#FFFFFF";
    }
  }};
  background-color: ${({ backColor = "transparent" }) => {
    switch (backColor) {
      case "transparent":
        return "transparent";
      case "red":
        return "#E13B39";
    }
  }};

  ${(props) =>
    props.border &&
    css`
      border: 2px solid #e13b39;
    `};
`;

const UniversalButton = ({ children, ...props }: Props) => {
  return <StyledButton {...props}>{children}</StyledButton>;
};

export { UniversalButton };
