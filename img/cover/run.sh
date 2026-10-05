#!/bin/bash

pre="https://img.pterclub.com/images/2022/08/26/spider"

for i in {20..21}; do
# for i in {1..3}; do
# for i in {3..19}; do
    echo $i
    fig_url="${pre}${i}.jpg"
    # fig_url="${pre}${i}.png"
    wget ${fig_url}
done
