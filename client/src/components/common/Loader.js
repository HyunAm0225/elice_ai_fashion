import React from "react";
import styled from "styled-components";

const Loading = styled.div`
  @keyframes ldio-gri7c0xz2ji {
    0% {
      transform: translate(-50%, -50%) rotate(0deg);
    }
    100% {
      transform: translate(-50%, -50%) rotate(360deg);
    }
  }
  .ldio-gri7c0xz2ji div {
    position: absolute;
    width: 20px;
    height: 20px;
    border: 6px solid #e0e3da;
    border-top-color: transparent;
    border-radius: 50%;
  }
  .ldio-gri7c0xz2ji div {
    animation: ldio-gri7c0xz2ji 1s linear infinite;
    top: 100px;
    left: 100px;
  }
  .loadingio-spinner-rolling-wallm3yarlg {
    width: 200px;
    height: 200px;
    display: inline-block;
    overflow: hidden;
    position: absolute;
    left: 50%;
    margin-left: -100px;
  }
  .ldio-gri7c0xz2ji {
    width: 100%;
    height: 100%;
    position: relative;
    transform: translateZ(0) scale(1);
    backface-visibility: hidden;
    transform-origin: 0 0; /* see note above */
  }
  .ldio-gri7c0xz2ji div {
    box-sizing: content-box;
  }
`;

export const Loader = () => {
  return (
    <div
      style={{
        display: "flex",
        justifyContent: "center",
        width: "100%",
        height: "100%",
        position: "relative",
      }}
    >
      <Loading>
        <div className="loadingio-spinner-rolling-wallm3yarlg">
          <div className="ldio-gri7c0xz2ji">
            <div></div>
          </div>
        </div>
      </Loading>
    </div>
  );
};
