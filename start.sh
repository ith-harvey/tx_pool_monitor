#!/usr/bin/env bash
export CURRENT_DIR=$(pwd)

dir="$(dirname "$0")"
source $dir/_virtualenv/bin/activate || exit
export PYTHONPATH=$PYTHONPATH:$dir:$dir/lib/pymaker:

exec python3 -m tx_pool_monitor \
  --eth-from "0x5F5080599A217Cf778cD45c21a14f621e5f21701" \
  --eth-key "key_file=${CURRENT_DIR?:}/test_acc.json,pass_file=${CURRENT_DIR?:}/test_acc.pass" \
  --web3-address "206.81.1.77:8545"
