import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
    mobileRoot: {
      textAlign: "center",
      padding: theme.spacing(1),
      flexGrow: 1,
    },
    mobileNavbar: {
      height: "6vh",
      textAlign: "right",
      backgroundColor: "#f8f8f8",
      padding: "10px",
    },
    mobileProfileIcon: {
      fontSize: "40px",
    },
    mobileRecommendMessageBox: {
      height: "6vh",
      textAlign: "left",
    },
    mobileRecommendMessage: {
      fontSize: "18px",
      fontWeight: "bold",
    },
    mobileRecommendInfoBox: {
      height: "34vh",
    },
    mobileRecommendImageBox: {
      padding: "10px",
    },
    mobileImageBox: {
      height: "34vh",
      borderRadius: "15px",
      borderColor: "black",
      marginBottom: "10px"
    },
  
    // mobileImage: {
    //   objectFit: "cover",
    //   height: "100%",
    //   width: "100%",
    //   borderRadius: "15px",
    // },
    mobileImage: {
      objectFit: "cover",
      height: "100%",
      width: "100%",
      borderRadius: "15px",
    },
    mobileRecommendTextBox: {
      padding: "10px",
      textAlign: "left",
    },
    mobileBrandFavoriteBox: {
      height: "30px",
      display: "flex",
      justifyContent: "space-between",
    },
    mobileBrandName: {
      fontWeight: "bold",
      fontSize: "18px",
    },
    mobileDescription: {
      height: "60%",
    },
    mobileShortDescription:{
      overflow: "hidden",
      whiteSpace: "nowrap",
      textOverflow: "ellipsis",
    },
    mobileDiscountPriceBox: {
      display: "flex",
      justifyContent: "space-between",
      fontSize: "25px",
    },
    mobileDiscount: {
      fontWeight: "bold",
      color: "red",
    },
    mobilePrice: {
      fontWeight:"bold"
    },
    mobileCategoryContainer: {
        display: "flex",
        height: "8vh",
        borderTop: "1px solid #E0E3DA",
        borderBottom: "1px solid #E0E3DA",
        whiteSpace: "nowrap",
        overflowX: "auto",
        overflowY: "hidden"
    },
    mobileCategoryButton: {
        border: "1px solid #e6e6e6",
        borderRadius: "15px",
        margin: "10px 6px",
        backgroundColor: "#E0E3DA",
        fontWeight: "700",
        fontSize: "14px",
        paddingTop: "2px",
        paddingBottom: "2px",
        "&:hover, &:focus, &:active": {
            backgroundColor: "#566270",
            color: "white"
          },
    },
    mobileCategoryActiveButton: {
      border: "1px solid #e6e6e6",
      borderRadius: "15px",
      margin: "10px 6px",
      backgroundColor: "#566270",
      color: "white",
      fontWeight: "700",
      fontSize: "14px",
      paddingTop: "2px",
      paddingBottom: "2px",
      "&:hover, &:focus, &:active": {
        backgroundColor: "#566270",
        color: "white"
      },
    }
  }));


export default useStyles;