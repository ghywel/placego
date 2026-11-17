#!/bin/bash
log="/share/log.txt"
#log="/dev/null"

#if transcode bitrate less than 299999 detected intercept, otherwise pass to ffmpeg8 unmodified
regex="-b:v [0-2][0-9]{5} " 
if [[ "$*" =~ $regex ]]; then 
	echo -ne "\n\n--------------------------------------------------------------\n$(date)\n" >> $log
	echo -ne "---COMMAND INTERCEPTED---\n$*\n\n" >> $log
	#input indexes
	indexSS=0
	indexFilePath=0
	#output hls indexes
	indexInputF=0
	indexOutputF=0
	indexMaxDelay=0
	indexHLSTime=0
	indexHLSSegmentType=0
	indexHLSfmp4InitFilename=0
	indexStartNumber=0
	indexHLSSegmentFilename=0
	indexHLSPlaylistType=0
	indexHLSListSize=0
	indexHLSSegmentOptions=0
	indexY=0

	inputFilePath=""

	#loop args and extract relevant flags
	#TODO try a subtraction algorithm to preserve as many flags as possible, support subtitles etc.
	argIndex=1
	for arg in "$@"
	do
		#echo "arg is: [$arg]" >> $log

  		case "$arg" in
  			"-ss")
    			echo "-ss input flag found at index [$argIndex] " >> $log
    			indexSS=$((argIndex+1))
    			;;
  			"-i")
    			echo "-i input flag found at index [$argIndex] " >> $log
    			indexFilePath=$((argIndex+1))
    			inputFilePath=${!indexFilePath}
    			echo "Input file path is: [$inputFilePath]" >> $log
    			;;

    		"-f")
    			echo "-f flag found at index [$argIndex] " >> $log
  				if [[ $indexFilePath -eq 0 ]]; then
  					echo "flag before input, setting input -f" >> $log
  					indexInputF=$((argIndex+1))
  				else
  					echo "flag after input, setting output -f" >> $log
  					indexOutputF=$((argIndex+1))
  				fi
    			;;
    		"-max_delay")
    			echo "-max_delay flag found at index [$argIndex] " >> $log
    			indexMaxDelay=$((argIndex+1))
    			;;
    		"-hls_time")
    			echo "-hls_time flag found at index [$argIndex] " >> $log
    			indexHLSTime=$((argIndex+1))
    			;;
    		"-hls_segment_type")
    			echo "-hls_segment_type flag found at index [$argIndex] " >> $log
    			indexHLSSegmentType=$((argIndex+1))
    			;;
    		"-hls_fmp4_init_filename")
    			echo "-hls_fmp4_init_filename flag found at index [$argIndex] " >> $log
    			indexHLSfmp4InitFilename=$((argIndex+1))
    			;;
    		"-start_number")
    			echo "-start_number flag found at index [$argIndex] " >> $log
    			indexStartNumber=$((argIndex+1))
    			;;
    		"-hls_segment_filename")
    			echo "-hls_segment_filename flag found at index [$argIndex] " >> $log
    			indexHLSSegmentFilename=$((argIndex+1))
    			;;
    		"-hls_playlist_type")
    			echo "-hls_playlist_type flag found at index [$argIndex] " >> $log
    			indexHLSPlaylistType=$((argIndex+1))
    			;;
    		"-hls_list_size")
    			echo "-hls_list_size flag found at index [$argIndex] " >> $log
    			indexHLSListSize=$((argIndex+1))
    			;;
    		"-hls_segment_options")
    			echo "-hls_segment_options flag found at index [$argIndex] " >> $log
    			indexHLSSegmentOptions=$((argIndex+1))
    			;;
  			"-y")
    			echo "-y flag found at index [$argIndex] " >> $log
    			indexY=$((argIndex+1))
    			;;
    	esac
    	argIndex=$((argIndex+1))
    done

    newCommand=$'-analyzeduration
    200M
	-probesize
	1G\n'
	if [ $indexSS -ne 0 ]; then #include input seek flag if provided
		newCommand+=$'-ss\n'
		newCommand+="${!indexSS}"
		newCommand+=$'\n'
	fi
	newCommand+="-init_hw_device
    drm=dr:/dev/dri/renderD129
    -init_hw_device
    vaapi=va@dr
    -init_hw_device
    vulkan=vk@dr
    -filter_hw_device
    vk
    -hwaccel
    vaapi
    -hwaccel_output_format
    vaapi
    -i
    ${!indexFilePath}
    -c:a
    libfdk_aac
    -ac
    2
    -ab
    256000
    -af
    volume=2
    -copyts
    -c:v
    hevc_vaapi
    -tag:v
    hvc1
    -global_quality
    20
    -low_power
    1
    -sei
    -a53_cc
    -force_key_frames
    expr:gte(t,n_forced*3)
    -avoid_negative_ts
    disabled
    -max_muxing_queue_size
    2048
    -f
    ${!indexOutputF}
    -max_delay
    ${!indexMaxDelay}
    -hls_time
    ${!indexHLSTime}
    -hls_segment_type
    ${!indexHLSSegmentType}
    -hls_fmp4_init_filename
    ${!indexHLSfmp4InitFilename}
    -start_number
    ${!indexStartNumber}
    -hls_segment_filename
    ${!indexHLSSegmentFilename}
    -hls_playlist_type
    ${!indexHLSPlaylistType}
    -hls_list_size
    ${!indexHLSListSize}
    -hls_segment_options
    ${!indexHLSSegmentOptions}
    -y
    ${!indexY}"

    #Build new command string into an array
    declare -a newCommandBuilder
   	while read line; 
    do 
    	newCommandBuilder+=("$line"); 
    done < <(echo "$newCommand") #weird syntax to preserve spaces in filepath

    echo -ne "\nMODIFIED command:\n" >> $log
    echo -ne "${newCommandBuilder[*]}\n\n" >> $log
    #echo -ne "\n" >> $log

	/usr/lib/jellyfin-ffmpeg/ffmpeg8 "${newCommandBuilder[@]}" 2>> $log
else
	echo "ffmpeg: NORMAL PASSTHROUGH" >> $log
	/usr/lib/jellyfin-ffmpeg/ffmpeg8 "$@" #2>> $log
fi