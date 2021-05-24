import { Box } from "@material-ui/core";
import useStyles from "../../styles/MyPageStyle";

function Footer() {
  const classes = useStyles();
  return (
    <Box className={classes.mobileFooterBox}>
      <Box className={classes.mobileFooterText}>
        클로젯은 상품에 직접 관여하지 않으며 상품 주문, 배송 및 환불의 의무와
        책임은 각 판매업체에 있습니다.
      </Box>
    </Box>
  );
}

export default Footer;
