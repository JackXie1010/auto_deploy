/*
 Navicat Premium Data Transfer

 Source Server         : xzj
 Source Server Type    : MySQL
 Source Server Version : 80013
 Source Host           : localhost:3306
 Source Schema         : server

 Target Server Type    : MySQL
 Target Server Version : 80013
 File Encoding         : 65001

 Date: 11/05/2019 20:16:35
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for server
-- ----------------------------
DROP TABLE IF EXISTS `server`;
CREATE TABLE `server`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `host` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `projectDir` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `isOnline` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `addTime` datetime(0) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of server
-- ----------------------------
INSERT INTO `server` VALUES (1, 'deploy', 'root@a.a.aa.aa', 'aaa', '/home/pro/deploy', 1, 1, '2019-02-22 10:09:07');
INSERT INTO `server` VALUES (2, 'deploy2', 'root@a.a.aa.aa', 'aaaaa', '/home/pro/deploy2', 0, 1, '2019-02-19 14:54:33');
INSERT INTO `server` VALUES (5, 'aaa', 'ccc', '1', 'bbbc', 1, 0, '2019-05-11 13:03:38');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, 'root', '468053be748a5928e14147c89cb1eda9');

SET FOREIGN_KEY_CHECKS = 1;
