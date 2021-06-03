import React from "react";
import { Box } from "@material-ui/core";
import { Mobile } from "MediaQuery";

import Navbar from "components/common/Navbar";
import StyleBook from "components/MyPage/StyleBook";
import Shopping from "components/MyPage/Shopping";
import Information from "components/MyPage/Information";
import Welcome from "components/MyPage/Welcome";
import Footer from "components/MyPage/Footer";
import { useHistory } from "react-router-dom";

// url을 통한 다른 사용자 접근 통제 필요
function MyPage() {
  const history = useHistory();
  if (localStorage.getItem("jwt") === null) {
    history.push("/login");
  }

  return (
    <Mobile>
      <Navbar />
      <Box className="mobileBigPaddingBox">
        <Welcome />
        <StyleBook />
        <Shopping />
        <Information />
        <Footer />
      </Box>
    </Mobile>
  );
}

export default MyPage;
