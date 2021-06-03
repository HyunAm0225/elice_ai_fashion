import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  mobileAppBar: {
    background: "rgba(256, 256, 256, 1)",
    position: "static",
  },
  mobileGrow: {
    flexGrow: "1",
  },
  mobileNavbarSelect: {
    fontWeight: "bold",
    color: "var(--color-main-b)",
  },
  mobileNavbarSkip: {
    fontWeight: "bold",
    color: "var(--color-bg-light)",
  },
  mobileImageButton: {
    height: "180px",
    backgroundColor: "var(--color-bg-light)",
    borderRadius: "15px",
    justifyContent: "center",
    alignContent: "center",
    outline: "none",
  },
}));

export default useStyles;
